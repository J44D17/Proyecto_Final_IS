#-*- coding: utf-8 -*-

from django import db
from django.db import models

class Evento(models.Model):

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

    fechaEvento = models.CharField(
        max_length=30,
        null=False,
        db_column='fecha_evento'
    )
    ubicacion = None
    categoria = None

    class Meta:
        db_table = 'eventos'


