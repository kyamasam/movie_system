from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from apps.users.models import User
from apps.users.serializers.user_serializer import UserCreateUpdateSerializer, UserListSerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.db import transaction
from apps.users.utils import get_tokens_for_user
class UserViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    
    def get_permissions(self):
        if self.action=="create":
            return [AllowAny()]
        
        return [IsAuthenticated()]
    
    def get_serializer_class(self):
        if self.action =="create" or self.action =="update":
            return UserCreateUpdateSerializer
        return UserListSerializer
        

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return User.objects.all()
        return User.objects.filter(id=user.id)
    
    def retrieve(self, request, pk=None, *args, **kwargs):
        user = self.get_object()
        return Response(self.get_serializer(user).data)
    
    def list(self, request, *args, **kwargs):
        users = self.get_queryset()
        return Response(self.get_serializer(users, many=True).data)
    
    @transaction.atomic
    def update(self, request, pk=None,  *args, **kwargs):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response("user not found", status=status.HTTP_404_NOT_FOUND)
        data = request.data
        serializer = self.get_serializer(user, data=data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        user_data=serializer.instance
        return Response(self.get_serializer(user_data).data, status=status.HTTP_200_OK)

    
    @transaction.atomic
    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        user_data=serializer.instance
        
        token_data = get_tokens_for_user(serializer.instance)
        user_data.token=token_data.get('access')
        user_data.refresh=token_data.get('refresh')
        response_serializer = self.get_serializer(user_data)
     
        
        return Response(response_serializer.data)
        
    
