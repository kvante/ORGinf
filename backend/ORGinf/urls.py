from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView, TokenVerifyView,
)


urlpatterns = [
    path('admin/', admin.site.urls),

   path('', include('app.urls')),
   path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
   path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
   path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

   path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
   path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
   path('auth/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

]

