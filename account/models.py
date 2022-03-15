from django.db import models
from django.conf import settings
from django.urls import reverse


class Profile(models.Model):
    """
    User profile.
    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    bio = models.TextField(null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    profile_pic = models.ImageField(upload_to='images/profile', blank=True)
    facebook_url = models.CharField(max_length=150, null=True, blank=True)
    website_url = models.CharField(max_length=150, null=True, blank=True)
    twitter_url = models.CharField(max_length=150, null=True, blank=True)
    instagram_url = models.CharField(max_length=150, null=True, blank=True)
    github_url = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return f'Profile for user {self.user.username}'

    
    def get_absolute_url(self):
        return reverse('account:dashboard')
