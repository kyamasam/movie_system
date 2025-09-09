from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from apps.users.models import User
from apps.users.serializers.user_serializer import UserCreateSerializer, UserSerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.db import transaction
from apps.users.utils import get_tokens_for_user
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    # permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    
    def get_permissions(self):
        if self.action=="create":
            return [AllowAny()]
        
        return [IsAuthenticated()]
        

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return User.objects.all()
        return User.objects.filter(id=user.id)
    
    @transaction.atomic
    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = UserSerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        user_data=serializer.instance
        
        token_data = get_tokens_for_user(serializer.instance)
        user_data.token=token_data.get('access')
        user_data.refresh=token_data.get('refresh')
        response_serializer = UserCreateSerializer(user_data)
     
        
        return Response(response_serializer.data)
        
    
