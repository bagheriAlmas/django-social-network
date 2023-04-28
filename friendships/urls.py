from django.urls import path
from .views import UserListView, RequestView, RequestListView, AcceptView

urlpatterns = [
    path('users/', UserListView.as_view(), name='users-list'),
    path('request/', RequestView.as_view(), name='request'),
    path('requests-list/', RequestListView.as_view(), name='request-list'),
    path('accept/', AcceptView.as_view(), name='accept'),
    # path('friends/'),
]
