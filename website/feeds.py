from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from django.urls import reverse_lazy
from .models import Post


class LatestPostsFeed(Feed):
    title = "My Site"
    link = reverse_lazy("website:blog")
    description = "New posts of my blog"

    def items(self):
        return Post.objects.all().filter(status="published")

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.body, 30)
