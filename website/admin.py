from django.contrib import admin

from .models import Post, PostComment, Category



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    Customizing display of the Post Model
    """
    list_display = ('title', 'slug', 'author', 'published', 'status')
    list_filter = ('status', 'created', 'published', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    # raw_id_fields = ('author',)
    date_hierarchy = 'published'
    ordering = ('status', 'published')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Customizing category Model display.
    """
    ordering = ('name',)

    
@admin.register(PostComment)
class PostCommentAdmin(admin.ModelAdmin):
    """
    Comment admin interface manager.
    """
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')
