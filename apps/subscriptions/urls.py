from rest_framework.routers import DefaultRouter
# from apps.users.views.user_view import UserViewSet
from django.urls import path, include


user_router = DefaultRouter()
# user_router.register(r'users', UserViewSet)

urlpatterns = [
    
]
urlpatterns += user_router.urls
