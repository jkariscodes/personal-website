from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField

from autoslug.fields import AutoSlugField

User = get_user_model()

class Category(models.Model):
    """
    Post categories.
    """
    name = models.CharField(max_length=30, default='Uncategorized')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """
        Canonical URL for the category
        """
        return reverse('website:home', args=self.name)


class Post(models.Model):
    """Post model"""
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='title', unique=True, editable=True)
    # body = models.TextField()
    body = RichTextField(blank=True, null=True)
    published = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default='uncategorized')
    snippet = models.CharField(max_length=255)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='draft'
    )

    def get_absolute_url(self):
        """
        Return the canonical URL of the post.
        """
        return reverse('website:article-detail', args=[self.slug])

    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return self.title + ' | ' + str(self.author)


class PostComment(models.Model):
    """
    Comment for blog posts.
    """
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments'
    )
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'
