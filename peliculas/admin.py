from django.contrib import admin
from .models import tablaPersona, tablaPelicula, tablaPremio, tablaRelaciones

# Register your models here.

admin.site.register(tablaPersona)
admin.site.register(tablaPelicula)
admin.site.register(tablaPremio)
admin.site.register(tablaRelaciones)
