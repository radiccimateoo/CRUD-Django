from django.contrib import admin
from .models import tablaPersona, tablaPelicula, tablaPremio

# Register your models here.
class Persona(admin.ModelAdmin):
    list_filter = ('nombre', 'apellido', 'nacimiento', 'dni', 'sueldo_mensual', )

class Pelicula(admin.ModelAdmin):
    list_filter = ('nombre_pelicula', 'descripcion', 'genero', 'persona', )

class Premio(admin.ModelAdmin):
    list_filter = ('premio_ganador', 'cantidad_nominaciones', 'pelicula')


admin.site.register(tablaPersona, Persona)
admin.site.register(tablaPelicula, Pelicula)
admin.site.register(tablaPremio, Premio)