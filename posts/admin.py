from django.contrib import admin
from .models import Post, PostFile


class PostFileInline(admin.TabularInline):
    model = PostFile
    fields = ['file', ]
    extra = 0


class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ['title', 'is_active', 'is_public', 'created_at', 'updated_at']
    inlines = [PostFileInline, ]


admin.site.register(Post, PostAdmin)
