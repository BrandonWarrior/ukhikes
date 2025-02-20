from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'status')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_at')
    prepopulated_fields = {'slug': ('title',)}

