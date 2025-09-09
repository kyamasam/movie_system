from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from apps.users.models import User
from apps.users.serializers.user_serializer import UserSerializer

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return User.objects.all()
        return User.objects.filter(id=user.id)
