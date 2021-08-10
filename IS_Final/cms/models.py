#-*- coding: utf-8 -*-

from django.db import models
from .authManager import UsuarioManager

class Persona(models.Model):

    TIPO_PERSONA = [
        (1, 'ADMINISTRADOR'),
        (2, 'CAJERO')
    ]
    personaId = models.AutoField(
        primary_key=True,
        null=False,
        unique=True,
        db_column='id'
    )
    personaNombre = models.CharField(
        max_length=30,
        null=False,
        db_column='nombre',
        verbose_name='Nombre de la persona',
        help_text='Aqui va el nombre de la persona'
    )
    personaApellido = models.CharField(
        max_length=30,
        null=False,
        db_column='apellido',
        verbose_name='Apellido de la persona',
        help_text='Aqui va el apellido de la persona'
    )
    correo = models.EmailField(
        max_length=50,
        db_column='correo',
        null=False,
        verbose_name='Correo del lector',
        help_text='Debes ingresar un correo valido',
    )
    password = models.TextField()
    class Meta:
        pass