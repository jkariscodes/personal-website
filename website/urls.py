from django.urls import path
from .views import PostView, home, ArticleView

app_name = 'blog'

urlpatterns = [
    path('', home, name='home'),
    path('blog/', PostView.as_view(), name='blog'),
    path('article/<slug:slug>', ArticleView.as_view(), name='article-detail'),
]
