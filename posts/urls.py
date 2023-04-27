from django.urls import path
from .views import PostView,PostListView

urlpatterns = [
    path('post/', PostView.as_view(), name='post'),
    path('post/<int:pk>/', PostView.as_view(), name='post-detail'),
    path('posts/', PostListView.as_view(), name='post-list'),
]
