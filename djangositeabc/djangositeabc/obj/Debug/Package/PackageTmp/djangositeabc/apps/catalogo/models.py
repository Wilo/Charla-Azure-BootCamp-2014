# -*- coding: utf-8
from django.db import models
from datetime import date,datetime
# Create your models here.

class Ciudadela(models.Model):
    Descripcion = models.CharField(max_length=45, verbose_name="Descripcion")
    Fecha= models.DateTimeField(default=datetime.today(), verbose_name="Fecha de Creacion")

    def __unicode__(self):
        return self.Descripcion

    class Meta:
        ordering= ('Descripcion',)
        db_table= 'demo_MCiudadela'