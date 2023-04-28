from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render

from friendships.models import Friendship
from friendships.serializers import UserListSerializer

User = get_user_model()


class UserListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        users = User.objects.filter(is_superuser=False, is_staff=False, is_active=True)
        serializer = UserListSerializer(users, many=True)
        return Response(serializer.data)


class RequestView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user_id = request.data.get('user')
        user = get_object_or_404(User, pk=user_id)
        Friendship.objects.get_or_create(request_from=request.user, request_to=user)
        return Response({'detail': 'Request Send'}, status=status.HTTP_201_CREATED)


class RequestListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        friendship = Friendship.objects.filter(request_to=request.user, is_accepted=False)
        users = [fr.request_from for fr in friendship]
        serializer = UserListSerializer(users, many=True)
        return Response(serializer.data)


class AcceptView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user_id = request.data.get('user')
        try:
            user = User.objects.get(pk=user_id)
            friendship = Friendship.objects.get(request_from=user, request_to=request.user, is_accepted=False)
        except (User.DoesNotExist, Friendship.DoesNotExist):
            return Response({'detail': 'user not found'},status=status.HTTP_400_BAD_REQUEST)

        friendship.is_accepted = True
        friendship.save()

        return Response({'detail': 'Connected'}, status=status.HTTP_200_OK)
