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
    genero = models.CharField(max_length=200)
    persona = models.ForeignKey(tablaPersona, models.CASCADE, blank=True, null=True)

    def __str__(self):
        return "{}".format(self.nombre_pelicula)

class tablaPremio(models.Model):
    cantidad_nominaciones = models.IntegerField()
    pelicula = models.ForeignKey(tablaPelicula, models.CASCADE, blank=True, null=True)

    def __str__(self):
        return "{}".format(self.premio_ganador)

class tablaImagenes(models.Model):
    base = models.CharField(blank=True, null=True, max_length=20000000)

    def __str__(self):
        return "{}".format(self.base)

class tablaCines(models.Model):
    nombre = models.CharField(max_length=400)
    direccion = models.CharField(max_length=400)
    latitud = models.CharField(max_length=400, null=False, blank=False, default='122')
    longitud = models.CharField(max_length=400, null=False, blank=False, default='122')
    telefono = models.PositiveIntegerField()
    web = models.CharField(max_length=400)