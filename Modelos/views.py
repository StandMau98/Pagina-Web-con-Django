from django.shortcuts import render
from django.template import Template
from Modelos.models import *


# Create your views here.
def inicio(request):
    return render(request,"Modelos/index.html")

def creacion_abertura(request):
    if request.method == "POST":
        nombre_ventanas = request.POST["Ventanas"]
        numero_medida = request.POST["Medidas"]
        nombre_color = request.POST["Color"]

        Ventanas= Ventanas(nombre= nombre_ventanas, medida= numero_medida, color= nombre_color)
        Ventanas.save()

    return render(request,"Modelos/nueva_abertura.html")

def Ventana(request):
    return render(request,"Modelos/Ventanas.html")

def Puertas(request):
    return render(request,"Modelos/Puertas.html")

def mosquiteros(request):
    return render(request,"Modelos/mosquiteros.html")

