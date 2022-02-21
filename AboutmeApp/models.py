from ssl import create_default_context
from django.db import models

# Create your models here.

class Aboutme(models.Model):
    titulo = models.CharField(max_length=40)
    contenido = models.CharField(max_length=400)
    imagen = models.ImageField(upload_to = 'Aboutme')

    class Meta:
        verbose_name = 'aboutme'
        verbose_name_plural = 'aboutmes'
    
    def __str__(self):
        return self.titulo
    
    