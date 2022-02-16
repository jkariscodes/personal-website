from django.urls import path
from .views import PostView, home, ArticleView

urlpatterns = [
    path('', home, name='home'),
    path('blog/', PostView.as_view(), name='blog'),
    path('article/<int:pk>', ArticleView.as_view(), name='article-detail'),
]
