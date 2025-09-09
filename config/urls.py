from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from apps.users.urls import urlpatterns as users_url_patterns
from apps.subscriptions.urls import urlpatterns as subscriptions_url_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include([
            *users_url_patterns,
            *subscriptions_url_patterns,
        ])),
    # YOUR PATTERNS
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

