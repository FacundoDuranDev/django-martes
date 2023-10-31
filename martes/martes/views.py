from django.views import View # revisar error META de la clase View
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, "home.html", {"nombres": ["Adrián", "Facundo","Raul","Ramiro","Roger"]})

def nombrar(request, nombre):
    return render(request, "nombrar.html", {"nombre": nombre})
