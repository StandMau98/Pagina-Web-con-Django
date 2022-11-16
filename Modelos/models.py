from django.db import models

class Ventanas(models.Model):
    nombre = models.CharField(max_length=50)
    medida = models.IntegerField()
    color = models.CharField(max_length=50)

