from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, render
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.views.generic import FormView
from .models import Post, PostComment, EmailMessage
from .forms import PostForm, EmailPostForm, CommentForm, ContactForm
from .serializers import PostSerializer, PostCommentSerializer


class HomePageView(TemplateView):
    """
    Website landing page.
    """

    template_name = "website/home.html"


class PostsListView(ListView):
    """
    Blog posts page.
    """

    model = Post
    template_name = "website/blog.html"
    ordering = ["-published"]
    paginate_by = 4


class PostArticleView(DetailView):
    """
    Post article page.
    """

    model = Post
    template_name = "../templates/website/article.html"


class AddCommentView(CreateView):
    """
    Add comment to post article.
    """

    model = PostComment
    form_class = CommentForm
    template_name = "../templates/website/article-comment.html"

    def form_valid(self, form):
        form.instance.post_id = self.kwargs["pk"]
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            "website:article-detail", kwargs={"slug": self.kwargs["slug"]}
        )


def post_share(request, post_slug):
    """
    Share blog post.
    """
    post = get_object_or_404(Post, slug=post_slug, status="published")
    sent = False

    if request.method == "POST":
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['name']} would recommend reading f{post.title}"
            message = f"Read {post.title} at {post_url}\n\n {cd['name']}'s comments: {cd['comments']}"
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [cd["to"]])
            sent = True
    else:
        form = EmailPostForm()
    return render(
        request, "website/share.html", {"post": post, "form": form, "sent": sent}
    )


class AddPostView(LoginRequiredMixin, CreateView):
    """
    Create new post article.
    """

    model = Post
    form_class = PostForm
    template_name = "website/post-new.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(AddPostView, self).form_valid(form)


class UpdatePostView(LoginRequiredMixin, UpdateView):
    """
    Update a given post article.
    """

    model = Post
    form_class = PostForm
    template_name = "website/edit-post.html"
    # fields = ['title', 'body', 'status']


class DeletePostView(DeleteView):
    """
    Delete a given post article.
    """

    model = Post
    template_name = "website/delete-post.html"
    success_url = reverse_lazy("website:blog")


class AboutPageView(TemplateView):
    template_name = "website/about.html"


class PortfolioPageView(TemplateView):
    template_name = "website/portfolio.html"


class ContactFormView(FormView):
    template_name = "website/contact.html"
    form_class = ContactForm
    success_url = reverse_lazy("website:success")

    def form_valid(self, form):
        email = form.cleaned_data["from_email"]
        subject = form.cleaned_data["subject"]
        message = form.cleaned_data["message"]
        msg = EmailMessage(email=email, subject=subject, message=message)
        msg.save()
        send_mail(subject, message, email, [settings.EMAIL_RECIPIENT])
        return super().form_valid(form)


class EmailSuccess(TemplateView):
    template_name = "website/success.html"


def category_view(request, cats):
    """
    Category view
    """
    category_posts = Post.objects.filter(category=cats.replace("-", " "))
    return render(
        request,
        "website/categories.html",
        {"cats": cats.title().replace("-", " "), "category_posts": category_posts},
    )


class PostListAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            "user": request.user.id,
            "title": request.data.get("title"),
            "category": request.data.get("category"),
            "body": request.data.get("body"),
            "snippet": request.data.get("snippet"),
            "status": request.data.get("status"),
        }
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetailAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return None

    def get(self, request, pk, *args, **kwargs):
        post = self.get_object(pk)
        if post is None:
            return Response(
                {"error": "Post not found"}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, *args, **kwargs):
        post = self.get_object(pk)
        if post is None:
            return Response(
                {"error": "Post not found"}, status=status.HTTP_404_NOT_FOUND
            )
        data = {
            "user": request.user.id,
            "title": request.data.get("title"),
            "body": request.data.get("body"),
            "snippet": request.data.get("snippet"),
            "status": request.data.get("status"),
        }
        serializer = PostSerializer(post, data=data, partial=True)
        if serializer.is_valid():
            if post.user.id == request.user.id:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(
                {"error": "You are not authorized to edit this post"},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        post = self.get_object(pk)
        if post is None:
            return Response(
                {"error": "Post not found"}, status=status.HTTP_404_NOT_FOUND
            )
        if post.user.id == request.user.id:
            post.delete()
            return Response({"res": "Object deleted!"}, status=status.HTTP_200_OK)
        return Response(
            {"error": "You are not authorized to delete this post"},
            status=status.HTTP_401_UNAUTHORIZED,
        )


class CommentAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return None

    def get(self, request, pk, *args, **kwargs):
        post = self.get_object(pk)
        if post is None:
            return Response(
                {"error": "Post not found"}, status=status.HTTP_404_NOT_FOUND
            )
        comments = PostComment.objects.filter(post=post)
        serializer = PostCommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk, *args, **kwargs):
        post = self.get_object(pk)
        if post is None:
            return Response(
                {"error": "Post not found"}, status=status.HTTP_404_NOT_FOUND
            )
        data = {
            "name": request.data.get("name"),
            "email": request.data.get("email"),
            "body": request.data.get("body"),
        }
        serializer = PostCommentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
