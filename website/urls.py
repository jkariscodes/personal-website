from django.urls import path
from . import views
from .feeds import LatestPostsFeed

app_name = 'website'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('contact/', views.contact_view, name='contact'),
    path('success/', views.success_view, name='success'),
    path('blog/', views.PostView.as_view(), name='blog'),
    # path('blog/categories/', views.CategoriesView.as_view(), name='categories'),
    # path('blog/category/<str:cats>/', views.category_view, name='category'),
    # path('blog/article/category-new/', views.AddCategoryView.as_view(), name='category-new'),
    path('blog/article/post-new/', views.AddPostView.as_view(), name='post-new'),
    path('blog/article/<slug:slug>/', views.ArticleView.as_view(), name='article-detail'),
    path('blog/article/<slug:slug>/edit/', views.UpdatePostView.as_view(), name='update_post'),
    path('blog/article/<int:pk>/<slug:slug>/comment/', views.AddCommentView.as_view(), name='comment_post'),
    path('blog/article/<slug:slug>/delete/', views.DeletePostView.as_view(), name='delete_post'),
    path('blog/article/<slug:post_slug>/share/', views.post_share, name='post_share'),
    path('feed/', LatestPostsFeed(), name='post_feed'),
]

