from django.contrib import admin

from .models import Post


admin.register(Post)
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
