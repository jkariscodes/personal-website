from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


def home(request):
    return render(request, 'home.html', {})


class PostView(ListView):
    model = Post
    template_name = 'blog.html'


class ArticleView(DetailView):
    model = Post
    template_name = 'article.html'

