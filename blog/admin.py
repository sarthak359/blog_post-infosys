# blog/admin.py
from django.contrib import admin
from .models import Post, Category, Comment

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0 # Don't show extra empty forms

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_on', 'last_modified')
    list_filter = ('categories', 'author')
    search_fields = ('title', 'content')
    inlines = [CommentInline]

admin.site.register(Post, PostAdmin)
admin.site.register(Category)

