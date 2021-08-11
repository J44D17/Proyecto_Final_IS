#-*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db.models.fields import IntegerField
from .authManager import UsuarioManager

class UsuarioModel(AbstractBaseUser, PermissionsMixin):

    TIPO_PERSONA = [
        (1, 'ADMINISTRADOR'),
        (2, 'USUARIO')
    ]
    usuarioId = models.AutoField(
        primary_key=True,
        unique=True,
        db_column='id'
    )

    usuarioNombre = models.CharField(
        max_length=20,
        null=False,
        db_column='nombre',
        verbose_name='Nombre del usuario'
    )

    usuarioApellido = models.CharField(
        max_length=20,
        null=False,
        db_column='apellido',
        verbose_name='Apellido del usuario'
    )

    usuarioCorreo = models.EmailField(
        db_column='correo',
        null=False,
        unique=True,
        verbose_name='Correo del usuario'
    )

    usuarioTipo = models.IntegerField(
        choices=TIPO_PERSONA,
        db_column='tipo',
        verbose_name='Tipo del usuario'
    )

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    # comportamiento del modelo al momento de realizar la creacion del superuser x consola  
    objects = UsuarioManager()

    # ahora defino que columna sera la encargada de valida que el usuario sea unico
    USERNAME_FIELD = 'usuarioCorreo'
    # sirve para indicar que campos se van a solicitar cuando se cree al superuser por consola
    REQUIRED_FIELDS = ['usuarioNombre', 'usuarioApellido', 'usuarioTipo']

    class Meta:
        db_table = 'usuarios'

class EventoModel(models.Model):

    TIPO_EVENTO = [
        (1, 'WORKSHOP'),
        (2, 'CONFERENCIA'),
        (3, 'SIMPOSIO'),
    ]
    PAIS = [
        (1, 'PERU'),
        (2, 'BRASIL'),
        (3, 'ARGENTINA'),
        (4, 'CHILE'),
        (5, 'MEXICO'),
    ]

    eventoId = models.AutoField(
        primary_key=True,
        unique=True,
        null=False,
        db_column='id'
    )

    fechaCreacion = models.DateTimeField(
        auto_now_add=True,
        db_column='fecha_creacion'
    )

    fechaEvento = models.DateField(
        blank=True,
        null=False,
        db_column='fecha_evento'
    )
    eventoTipo = models.IntegerField(
        choices=TIPO_EVENTO,
        db_column='tipo',
        verbose_name='Tipo del evento'
    )
    eventoLugar = models.IntegerField(
        choices=PAIS,
        db_column='lugar',
        verbose_name='Tipo del evento'
    )

    class Meta:
        db_table = 'eventos'