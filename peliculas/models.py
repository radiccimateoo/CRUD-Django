from django.db import models

# Create your models here.

class tablaPersona(models.Model):
    nacimiento = models.DateField()
    nombre = models.CharField(max_length=155)
    apellido = models.CharField(max_length=155)
    dni = models.IntegerField()
    sueldo_mensual = models.IntegerField() 

    def __str__(self):
        return "{}".format(self.nombre)

class tablaPelicula(models.Model):
    nombre_pelicula = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    base = models.BinaryField(blank=True)
    genero = models.CharField(max_length=200)
    persona = models.ForeignKey(tablaPersona, models.CASCADE, blank=True, null=True)

    def __str__(self):
        return "{}".format(self.nombre_pelicula)

class tablaPremio(models.Model):
    premio_ganador = models.CharField(max_length=200)
    cantidad_nominaciones = models.IntegerField()
    imagen = models.ImageField(blank=True)
    pelicula = models.ForeignKey(tablaPelicula, models.CASCADE, blank=True, null=True)

    def __str__(self):
        return "{}".format(self.premio_ganador)