from rest_framework import serializers

from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['user', 'title', 'description', 'is_active', 'is_public']
        extra_kwargs = {
            'user': {'read_only': True}
        }
