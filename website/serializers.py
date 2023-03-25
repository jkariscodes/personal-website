from rest_framework import serializers
from .models import Post, PostComment


class PostSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = Post
        fields = ("user", "title", "body", "published", "updated", "category", "slug")


class PostCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostComment
        fields = ("name", "email", "body", "created", "updated")
