from django.urls import path

from .views import (RegistroUsuarioController, CustomPayloadController, RegistroEventoController, EventosController
)
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView


urlpatterns = [
    path('registro', RegistroUsuarioController.as_view()),
    path('registraEvento', RegistroEventoController.as_view()),
    path('eventos', EventosController.as_view()),

    # Rutas del JWT
    path('login-custom', CustomPayloadController.as_view()),
    path('refresh-token', TokenRefreshView.as_view()),
    path('verify-token', TokenVerifyView.as_view()),
]