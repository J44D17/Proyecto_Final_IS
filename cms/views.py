from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListCreateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView)
from rest_framework.pagination import PageNumberPagination
from .serializers import *
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny, IsAuthenticated
import os
from django.conf import settings
import requests
from dotenv import load_dotenv
from django.db import transaction

load_dotenv()

class CustomPayloadController(TokenObtainPairView):
    """Sirve para modificar el payload de la token de acceso"""
    permission_classes = [AllowAny]
    serializer_class = CustomPayloadSerializer

    def post(self, request):
        data = self.serializer_class(data=request.data)
        if data.is_valid():
            print(data.validated_data)
            return Response(data={
                "success": True,
                "content": data.validated_data,
                "message": "Login exitoso"
            })

        else:
            # no indicara si es que el usario es incorrecto
            return Response(data={
                "success": False,
                "content": data.errors,
                "message": "error de generacion de la jwt"
            })


class RegistroUsuarioController(ListCreateAPIView):
    serializer_class = RegistroUsuarioSerializer

    def post(self, request: Request):
        data = self.serializer_class(data=request.data)
        if data.is_valid():
            data.save()
            return Response({
                "message": "Usuario Creado exitosamente",
                "content": data.data,
                "success": True
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({
                "message": "Error al crear el usuario",
                "content": data.errors,
                "success": False
            })

class RegistroEventoController(ListCreateAPIView):
    serializer_class = RegistroEventoSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request: Request):
        data = self.serializer_class(data=request.data)
        if data.is_valid():
            data.save()
            return Response({
                "message": "Evento Creado exitosamente",
                "content": data.data,
                "success": True
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({
                "message": "Error al crear el evento",
                "content": data.errors,
                "success": False
            })
class EventosController(ListAPIView):
    serializer_class = RegistroEventoSerializer
    queryset = EventoModel.objects.all()

class EventoController(RetrieveUpdateDestroyAPIView):
    queryset = EventoModel.objects.all()
    serializer_class = RegistroEventoSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request: Request, id):
        evento = EventoModel.objects.filter(eventoId=id).first()
        pruebaEvento = EventoModel.objects.values(
            'eventoId', 'eventoTipo', 'fechaEvento').filter(eventoId=id).first()
        # print(pruebaevento)
        if evento is not None:
            eventoSerializado = self.serializer_class(instance=evento)
            return Response(data={
                "success": True,
                "content": eventoSerializado.data,
                "message": None
            }, status=status.HTTP_200_OK)
        else:
            return Response(data={
                "message": "Evento no encontrado",
                "content": None,
                "success": False
            }, status=status.HTTP_404_NOT_FOUND)
    def put(self, request: Request, id):
        evento = EventoModel.objects.filter(eventoId=id).first()
        if evento:
            data = self.serializer_class(data=request.data)
            # initial_data => retorna todos los campos que hace match con el modelo PERO no valida las funciones de unique_together ni los indices ni los campos unique
            # si queremos 'pasarnos de vivos' y actualizar un registro con otro saltandonos las reglas del unique_together igual no se podra porque ahi la bd entrara a trabjar directamente a pesar que en el ORM lo permitase
            evento_actualizado = self.serializer_class().update(
                instance=evento, validated_data=data.initial_data)

            # print(evento_actualizado)
            return Response(data='ok')
        else:
            return Response(data={
                "message": "No se encontro el evento",
                "content": None,
                "success": False
            }, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request: Request, id):
        evento: EventoModel = EventoModel.objects.filter(eventoId=id).first()
        evento.save()
        # el metodo delete de la instancia elimina el registro de la bd y retornara, el total de registros eliminados
        # libro.delete()
        data = self.serializer_class(instance=evento)
        return Response(data={
            "success": True,
            "content": data.data,
            "message": "Se inhabilito el evento exitosamente"
        })