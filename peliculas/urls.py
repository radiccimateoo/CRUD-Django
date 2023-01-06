from django.urls import path
from .views import personaView, peliculaView, premioView, imagenesView, get

urlpatterns = [

    # PERSONAS
    path('registrarPersona/', personaView.registrarPersona, name='registrar'),
    path('guardarPersona/', personaView.procesarPersona, name='guardar'),
    path('', personaView.listarPersona, name='listaPersonas'),
    path('editarPersona/<int:id_persona>', personaView.editarPersona, name='editar'),
    path('actualizarPersona/<int:id_persona>', personaView.actulizarPersona, name='actualizar'),
    path('eliminarPersona/<int:id_persona>', personaView.eliminarPersona, name='eliminar'),
    path('funcionesSueldos/', personaView.funciones_sueldos, name='funcionesSueldos'),
    path('anual/<int:sueldo>', personaView.sueldo_anual, name='anual'),
    path('buscar/', personaView.filtrar, name='buscar'),
    path('edadActual/<int:anio_nacimiento>', personaView.edadActual, name='edadActual'),
    path('actualizarSueldo/<persona>/<int:sueldo>/<int:porcentaje>', personaView.actualizarSueldo, name='actualizarSueldo'),



    # PELICULAS
    path('registrarPelicula/', peliculaView.registrarPelicula, name='registrarPelicula'),
    path('guardarPelicula/', peliculaView.procesarPelicula, name='guardarPelicula'),
    path('listaPeliculas/', peliculaView.listarPelicula, name='listaPeliculas'),
    path('editarPelicula/<int:id_pelicula>', peliculaView.editarPelicula, name='editarPelicula'),
    path('actualizarPelicula/<int:id_pelicula>', peliculaView.actulizarPelicula, name='actualizarPelicula'),
    path('eliminarPelicula/<int:id_pelicula>', peliculaView.eliminarPelicula, name='eliminarPelicula'),


    # PREMIOS
    path('registrarPremio/', premioView.registrarPremio, name='registrarPremio'),
    path('guardarPremio/', premioView.procesarPremio, name='guardarPremio'),
    path('listaPremios/', premioView.listarPremio, name='listaPremios'),
    path('editarPremio/<int:id_premio>', premioView.editarPremio, name='editarPremio'),
    path('actualizarPremio/<int:id_premio>', premioView.actulizarPremio, name='actualizarPremio'),
    path('eliminarPremio/<int:id_premio>', premioView.eliminarPremio, name='eliminarPremio'),


    #EXTRAS
    path('imagenes/', imagenesView.imagenes, name='imagenes'),
    path('conversion/', imagenesView.convertir, name='conversion'),
    path('consulta/', personaView.consulta_join, name='consulta'),
    path('leer/', personaView.leerInsert, name='leer'),
    path('pdf', get, name='pdf'),
    

]