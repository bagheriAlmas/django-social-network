from django.urls import path
from .views import UserListView, RequestView, RequestListView

urlpatterns = [
    path('users/', UserListView.as_view(), name='users-list'),
    path('request/', RequestView.as_view(), name='request'),
    path('requests-list/', RequestListView.as_view(), name='request-list'),
    # path('accept/'),
    # path('friends/'),
]
