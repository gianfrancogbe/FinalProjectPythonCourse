from ssl import create_default_context
from django.db import models

# Create your models here.

class Alquila(models.Model):
    titulo = models.CharField(max_length=40)
    contenido = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to = 'alquila')
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now_add = True)
    
    class Meta:
        verbose_name = 'alquila'
        verbose_name_plural = 'alquilas'
    
    def __str__(self):
        return self.titulo
    
    