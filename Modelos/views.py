from django.shortcuts import render
from django.template import Template
from Modelos.models import Ventanas

# Create your views here.
def inicio(request):
    return render(request,"Modelos/index.html")

