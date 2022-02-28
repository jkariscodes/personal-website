from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post


def home(request):
    """
    Home page view.
    """
    return render(request, 'home.html', {})


class PostView(ListView):
    """
    Blog posts view.
    """
    model = Post
    template_name = 'blog.html'
    paginate_by = 5


class ArticleView(DetailView):
    """
    Single post view.
    """
    model = Post
    template_name = 'article.html'


class AddPostView(CreateView):
    """
    Create blog post view.
    """
    model = Post
    form_class = PostForm
    template_name = 'post-new.html'
    # fields = ('title', 'body', 'status', 'author')
    # fields = '__all__'


class UpdatePostView(UpdateView):
    """
    Update blog post view.
    """
    model = Post
    template_name = 'edit-post.html'
    fields = ['title', 'body', 'status']

