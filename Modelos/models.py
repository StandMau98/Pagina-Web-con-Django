from django.db import models

class Ventanas(models.Model):
    nombre = models.CharField(max_length=50)
    medida = models.IntegerField()
    color = models.CharField(max_length=50)

class Puertas(models.Model):
    nombre = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)

class mosquiteros(models.Model):
    nombre = models.CharField(max_length=50)
    medida = models.IntegerField()

