from django.urls import path
from .views import aboutme



urlpatterns = [
    

    path("aboutme/", aboutme, name="aboutme"),
    
    
]

