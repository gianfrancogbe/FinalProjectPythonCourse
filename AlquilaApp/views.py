from django.shortcuts import render
from AlquilaApp.models import Alquila

# Create your views here.
def alquila(request):
    alquila = Alquila.objects.all()
    return render(request, "AlquilaApp/alquila.html", {"alquila" : alquila})

