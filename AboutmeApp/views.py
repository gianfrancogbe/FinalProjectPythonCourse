from django.shortcuts import render
from .models import Aboutme

# Create your views here.

def aboutme(request):
    aboutme = Aboutme.objects.all()
    return render(request, "AboutmeApp/aboutme.html", {'aboutme': aboutme})
