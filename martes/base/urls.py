from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("agregar/<str:nombre>", views.añadir, name="añadir"),
    path("eliminar/<str:nombre>", views.eliminar, name="eliminar"),
    path("nombrar/", views.nombrar, name="nombrar")
]
