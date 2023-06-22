from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

from apps.users.views import ResetPasswordAPIView, PasswordResetConfirmAPIView
from root.settings import MEDIA_URL, MEDIA_ROOT
from root.swagger import swagger_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('apps.users.urls')),

    # JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/password/reset/', ResetPasswordAPIView.as_view(), name='password-reset'),
    path('api/password/reset/<str:token>/<str:uuid>/', PasswordResetConfirmAPIView.as_view(),
           name='password-reset-confirm'),

] + swagger_urls + static(MEDIA_URL, document_root=MEDIA_ROOT)
