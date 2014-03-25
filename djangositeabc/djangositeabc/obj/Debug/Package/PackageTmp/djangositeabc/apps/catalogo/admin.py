from django.contrib import admin
from .models import *

class AdminCiudadela(admin.ModelAdmin):
     list_display = ('id', 'Descripcion', 'Fecha',)

admin.site.register(Ciudadela,AdminCiudadela)