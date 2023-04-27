from django.conf import settings
from django.db import models


class Post(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    is_active = models.BooleanField(default=True)
    is_public = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        db_table = 'posts'

    def __str__(self):
        return self.title

class PostFile(models.Model):
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE)
    file = models.FileField(upload_to='files')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Post File'
        verbose_name_plural = 'Post Files'
        db_table = 'post_files'

    def __str__(self):
        return self.file.name