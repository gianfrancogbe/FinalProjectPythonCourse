from django.shortcuts import render, HttpResponse
# Create your views here.

def inicio(request):
    return render(request, "ProyectoWebApp/inicio.html")

def alquila(request):
    return render(request, "ProyectoWebApp/alquila.html")

def tienda(request):
    return render(request, "ProyectoWebApp/tienda.html")

def suscribete(request):
    return render(request, "ProyectoWebApp/suscribete.html")

def contacto(request):
    return render(request, "ProyectoWebApp/contacto.html")
