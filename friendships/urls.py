from django.urls import path
from .views import UserListView, RequestView

urlpatterns = [
    path('users/', UserListView.as_view(), name='users-list'),
    path('request/',RequestView.as_view(), name='request'),
    # path('requests-list/'),
    # path('accept/'),
    # path('friends/'),
]
