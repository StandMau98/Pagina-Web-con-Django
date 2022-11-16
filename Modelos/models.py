from django.db import models

class Ventanas(models.Model):
    nombre = models.CharField(max_length=50)
    medida = models.IntegerField(max_length=50)
    color = models.CharField(max_length=50)

