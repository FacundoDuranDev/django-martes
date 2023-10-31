from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def añadir(request, nombre=""):
    with open("registros.txt", "a") as file:
        file.write(nombre + ",")
        file.close()
    return HttpResponse("Añadido " + nombre + " al archivo registros.txt")


def eliminar(request, nombre=""):
    with open("registros.txt", "r") as file:
        raw_string = file.read()
        file.close()
    with open("registros.txt", "w") as file:
        file.write(raw_string.replace(nombre + ",", ""))
        file.close()
    return HttpResponse("Eliminado " + nombre + " del archivo registros.txt")


def nombrar(request):
    with open("registros.txt", "r") as file:
        raw_string = file.read()
        file.close()
    nombres = raw_string.split(",")
    return render(request, "nombrar.html", {"nombres": nombres})