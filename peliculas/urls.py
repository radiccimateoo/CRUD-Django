from django.urls import path
from .views import personaView, peliculaView, premioView, imagenesView

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
    path('actualizarSueldo/<int:sueldo>', personaView.actualizarSueldo, name='actualizarSueldo'),
    path('actualizarSueldoDiez/<int:sueldo>', personaView.actualizarSueldoDiez, name='actualizarSueldoDiez'),
    path('actualizarSueldoQuince/<int:sueldo>', personaView.actualizarSueldoQuince, name='actualizarSueldoQuince'),
    path('actualizarSueldoVeinte/<int:sueldo>', personaView.actualizarSueldoVeinte, name='actualizarSueldoVeinte'),


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

]