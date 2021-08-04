#-*- coding: utf-8 -*-

from django.db import models

class Evento(models.Model):
    class Meta:
        pass

    fecha = None
    ubicacion = None
    categoria = None


