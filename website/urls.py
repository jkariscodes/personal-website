from django.urls import path
from .views import PostView, home, ArticleView, AddPostView, UpdatePostView

app_name = 'blog'

urlpatterns = [
    path('', home, name='home'),
    path('blog/', PostView.as_view(), name='blog'),
    path('article/<slug:slug>', ArticleView.as_view(), name='article-detail'),
    path('blog/post-new/', AddPostView.as_view(), name='post-new'),
    path('blog/edit/<slug:slug>/', UpdatePostView.as_view(), name='update_post'),
]
