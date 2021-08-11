from django.urls import path
from django.urls.resolvers import path
from .views import (RegistroUsuarioController, CustomPayloadController
)
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('registro', RegistroUsuarioController.as_view()),
    path('eventos', RegistroUsuarioController.as_view()),

    # Rutas del JWT
    path('login-custom', CustomPayloadController.as_view()),
    path('refresh-token', TokenRefreshView.as_view()),
    path('verify-token', TokenVerifyView.as_view()),
]