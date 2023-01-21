from django.contrib import admin
from .models import tablaPersona, tablaPelicula, tablaPremio, tablaImagenes, tablaCines

# Register your models here.
class Persona(admin.ModelAdmin):
    list_filter = ('nombre', 'apellido', 'nacimiento', 'dni', 'sueldo_mensual', )

class Pelicula(admin.ModelAdmin):
    list_filter = ('nombre_pelicula', 'descripcion', 'genero', 'persona', )

class Premio(admin.ModelAdmin):
    list_filter = ('cantidad_nominaciones', 'pelicula')

class Cine(admin.ModelAdmin):
    list_filter = ('nombre','direccion', 'posicion_gps', 'telefono', 'web')


admin.site.register(tablaPersona, Persona)
admin.site.register(tablaPelicula, Pelicula)
admin.site.register(tablaPremio, Premio)
admin.site.register(tablaImagenes)
admin.site.register(tablaCines, Cine)