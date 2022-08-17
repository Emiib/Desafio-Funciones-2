from datetime import datetime
from django.http import HttpResponse
import datetime
from django.template import Context, Template



def saludar(request):
    return HttpResponse("Hola Mundo!")

def segunda_vista(request):
    return HttpResponse("<h1>Ya entendi! Esto es re simple!!!</h1>")



def dia_de_hoy(request):
    dia=datetime.datetime.today()
    cadena= "Hoy es " + str(dia)
    return HttpResponse(cadena)


def saludo_con_nombre(request, nombre):
    return HttpResponse("Hola mi nombre es: "+nombre)


def calcula_anio_nacimiento(request, edad):
    anio_nacimiento=2022 - int(edad)
    cadena="Anio nacimiento es: " + str(anio_nacimiento)
    return HttpResponse(cadena)

def probandohtml(request):
    miarchivo=open("D:/Documents/Proyectos python/Emiib/Proyectos y demas/Desafio-Funciones-2/Nuevo_Desafio/template.html")
    contenido=miarchivo.read()
    miarchivo.close()
    plantilla=Template(contenido)
    contexto=Context()
    documento=plantilla.render(contexto)
    return HttpResponse(documento)
