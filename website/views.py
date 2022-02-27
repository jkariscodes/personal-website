from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


def home(request):
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

