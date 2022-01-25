from django.urls import path
from ProyectoWebApp.views import alquila, contacto, inicio, suscribete, tienda

urlpatterns = [
    
    path("", inicio, name="inicio"),
    path("alquila/", alquila, name="alquila"),
    path("tienda/", tienda, name="tienda"),
    path("suscribete/", suscribete, name="suscribete"),
    path("contacto/", contacto, name="contacto"),
    
]
