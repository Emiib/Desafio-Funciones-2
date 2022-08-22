from datetime import datetime #esto fue para la funcion de "dia de hoy"
from django.http import HttpResponse
import datetime #esto fue para la funcion de "dia de hoy"
from django.template import loader #Context, #Template




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

    nom= 'Emiliano'
    ape= 'Borda' 
    diccionario={'nombre:',nom, 'apellido:',ape}
    plantilla=loader.get_template("template.html")
    documento=plantilla.render(diccionario)
    return HttpResponse(documento)
