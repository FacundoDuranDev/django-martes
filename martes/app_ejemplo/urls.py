from django.contrib import admin
from django.urls import path
from .views import ejemplo, nombrar

urlpatterns = [
    path('', ejemplo , name="ejemplo" ),
    path("asd",nombrar,name="nombrar")
]