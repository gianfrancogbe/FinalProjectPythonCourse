from django.contrib import admin
from .models import *
# Register your models here.

class AlquilaAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Alquila, AlquilaAdmin)