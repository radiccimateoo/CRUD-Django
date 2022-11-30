from django.db import models

# Create your models here.

class tablaPersona(models.Model):
    nacimiento = models.DateField()
    nombre = models.CharField(max_length=155)
    apellido = models.CharField(max_length=155)
    dni = models.IntegerField()
    sueldo_mensual = models.IntegerField()

    def __str__(self):
        return self.nombre

class tablaPelicula(models.Model):
    nombre_pelicula = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    genero = models.CharField(max_length=200)


    def __str__(self):
        return self.nombre_pelicula, self.genero

class tablaPremio(models.Model):
    nombre_premio = models.CharField(max_length=200)
    cantidad_nominaciones = models.IntegerField()
    cantidad_premios_ganados = models.IntegerField()

    def __str__(self):
        return self.nombre_premio


class tablaRelaciones(models.Model):
    persona = models.ForeignKey(tablaPersona, blank=False, null= False ,on_delete = models.CASCADE)
    pelicula = models.ForeignKey(tablaPelicula, blank=False, null= False ,on_delete = models.CASCADE)
    premio = models.ForeignKey(tablaPremio, blank=False, null= False ,on_delete = models.CASCADE)

    def __str__(self):
        return self.persona.nombre, self.pelicula.nombre_pelicula, self.premio.nombre_premio