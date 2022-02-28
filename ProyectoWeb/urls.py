"""ProyectoWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from ProyectoWebApp.views import login_request, LogoutView, register, editar_perfil,ProductoListView, ProductoDetalle,ProductoDelete,ProductoNuevo,ProductoUpdate



urlpatterns = [
        path('admin/', admin.site.urls),
        path('alquila/', include('AlquilaApp.urls')),
        path('contacto/', include('ContactoApp.urls')),
        path('aboutme/', include('AboutmeApp.urls')),
        path('blog/', include("BlogApp.urls")),
        path('login', login_request, name = 'Login'),
        path('logout', LogoutView.as_view(template_name='ProyectoWebApp/logout.html'), name = 'Logout'),
        path('registro', register, name = 'Registro'),
        path('edit/', editar_perfil, name='user_editar'),
        path('list/', ProductoListView.as_view(template_name='ProyectoWebApp/producto_lista.html'),name='productos'),
        path('detalle/<pk>', ProductoDetalle.as_view(),name = 'Detalle'),
        path('nuevo/', ProductoNuevo.as_view(),name='Crear'),
        path('update/<pk>', ProductoUpdate.as_view(), name='Actualizar'),
        path('delete/<pk>', ProductoDelete.as_view(),name='Borrar'),
        path('', include('ProyectoWebApp.urls'))
]
