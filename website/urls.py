from django.urls import path
from .views import (
    home,
    about,
    PostView,
    ArticleView,
    AddPostView,
    UpdatePostView,
    DeletePostView,
    post_share,
    contact_view,
    success_view,
    AddCategoryView,
    category_view,
    CategoriesView,
)
from .feeds import LatestPostsFeed

app_name = 'website'

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact_view, name='contact'),
    path('success/', success_view, name='success'),
    path('blog/', PostView.as_view(), name='blog'),
    path('blog/categories/', CategoriesView.as_view(), name='categories'),
    path('blog/category/<str:cats>/', category_view, name='category'),
    path('blog/article/post-new/', AddPostView.as_view(), name='post-new'),
    path('blog/article/category-new/', AddCategoryView.as_view(), name='category-new'),
    path('blog/article/<slug:slug>/', ArticleView.as_view(), name='article-detail'),
    path('blog/article/<slug:slug>/edit/', UpdatePostView.as_view(), name='update_post'),
    path('blog/article/<slug:slug>/delete/', DeletePostView.as_view(), name='delete_post'),
    path('blog/article/<slug:post_slug>/share/', post_share, name='post_share'),
    path('feed/', LatestPostsFeed(), name='post_feed'),
]

