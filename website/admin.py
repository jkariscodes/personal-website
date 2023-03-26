from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Post, PostComment, PostCategory, PortfolioProjects, EmailMessage


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Customizing display of the Post Model
    """

    summernote_fields = ("body",)
    list_display = ("title", "slug", "author", "published", "status")
    list_filter = ("status", "created", "published", "author")
    search_fields = ("title", "body")
    prepopulated_fields = {"slug": ("title",)}
    # raw_id_fields = ('author',)
    date_hierarchy = "published"
    ordering = ("status", "published")


@admin.register(PostCategory)
class PostCategoryAdmin(admin.ModelAdmin):
    """
    Customizing display of the Post Category Model
    """

    list_display = (
        "created",
        "updated",
        "title",
    )
    list_filter = ("title",)
    search_fields = ("title",)
    date_hierarchy = "created"
    ordering = ("created",)


@admin.register(PostComment)
class PostCommentAdmin(admin.ModelAdmin):
    """
    Comment admin interface manager.
    """

    list_display = ("name", "email", "post", "created", "active")
    list_filter = ("active", "created", "updated")
    search_fields = ("name", "email", "body")


@admin.register(PortfolioProjects)
class PortfolioProjectsAdmin(admin.ModelAdmin):
    list_display = ("title", "codebase", "live_project", "image")
    list_filter = ("title",)
    search_fields = ("title", "codebase", "live_project")


@admin.register(EmailMessage)
class EmailMessageAdmin(admin.ModelAdmin):
    list_display = ("email", "subject")
