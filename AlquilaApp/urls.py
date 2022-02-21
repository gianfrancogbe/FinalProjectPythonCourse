from django.urls import path
from AlquilaApp.views import alquila
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
   
    path("", alquila, name="alquila"),
    
]

