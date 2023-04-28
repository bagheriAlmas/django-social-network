from django.urls import path
from .views import PostView, PostListView, CommentView, LikeView

urlpatterns = [
    path('post/', PostView.as_view(), name='post'),
    path('post/<int:pk>/', PostView.as_view(), name='post-detail'),
    path('posts/', PostListView.as_view(), name='post-list'),
    path('posts/<int:pk>/comments/', CommentView.as_view(), name='comment'),
    path('posts/<int:pk>/likes/', LikeView.as_view(), name='like'),
]
