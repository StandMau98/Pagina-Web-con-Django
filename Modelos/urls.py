from django.urls import path
from Modelos.views import *

urlpatterns = [
    path("inicio/", inicio, name= "Base"),
    path("Ventanas/", Ventana, name="Ventanas"),
    path("nueva_abertura/", creacion_abertura, name="nuevo"),
    path("Puertas/", Puertas, name= "Puertas"),
    path("mosquiteros/",mosquiteros, name= "mosquiteros")
]