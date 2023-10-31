from django.shortcuts import render

# Create your views here.

def ejemplo(request):
    return render(request, "ejemplo.html", {"nombre": "Ramiro"})

def nombrar(request, nombre):
    return render(request, "nombrar.html", {"nombre": nombre})