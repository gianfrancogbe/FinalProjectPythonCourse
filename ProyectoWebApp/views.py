from django.shortcuts import render, HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.views import LogoutView
from AlquilaApp.models import Alquila
from .forms import UserRegisterForm, UserEditForm
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.

def inicio(request):
    return render(request, "ProyectoWebApp/inicio.html")

def login_request(request):
    if request.method=='POST':
        form= AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            usuario=form.cleaned_data.get('username')
            contra=form.cleaned_data.get('password')
            
            user = authenticate(username=usuario,password=contra)

            if user is not None:
                login(request,user)
                
                return render(request,'ProyectoWebApp/inicio.html', {'mensaje':f'Bienvenido {usuario}'})
            else:
                return render(request,'ProyectoWebApp/login.html',
            
                    {'form':form,
                    'error':'Valor ingresado incorrecto'})

        else:
           
            return render(request,'ProyectoWebApp/login.html',{'form':form})
    else:
        form=AuthenticationForm()
        return render(request,'ProyectoWebApp/login.html',{'form':form})
    

def register(request):
    if request.method == 'POST':
        formu = UserRegisterForm(request.POST)

        if formu.is_valid():
            username = formu.cleaned_data['username']
            formu.save()
            return HttpResponse(f'Usuario {username} creado correctamente')
    else:
        formu = UserRegisterForm()
    return render(request,'ProyectoWebApp/registro.html',{'formu': formu})

class UserCreate(CreateView):
    model = User
    success_url = reverse_lazy('Login')
    template_name='ProyectoWebApp/registro.html'
    form_class=UserRegisterForm



@login_required
def editar_perfil(request):
    usuario = request.user

    if request.method == 'POST':
        formulario = UserEditForm(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            usuario.email = data['email']
            usuario.password1 = data['password1']
            usuario.password2 = data['password2']
            usuario.save()
            return render(request,'ProyectoWebApp/inicio.html')

    else:
        formulario = UserEditForm({'email': usuario.email})

    return render(request,'ProyectoWebApp/editar_usuario.html',{'miform':formulario, 'usuario':usuario})


class ProductoListView(ListView):
    model=Alquila
    template_name='ProyectoWebApp/producto_lista.html'
    context_object_name='productos'

class ProductoDetalle(DetailView):
    model = Alquila
    template_name = 'ProyectoWebApp/producto_detalle.html'

class ProductoNuevo(CreateView):
    model = Alquila
    success_url = reverse_lazy('productos')
    fields = ['titulo','contenido']
    template_name = 'ProyectoWebApp/producto_nuevo.html'

class ProductoUpdate(UpdateView):
    model = Alquila
    success_url = reverse_lazy('productos')
    fields = ['titulo','contenido']
    template_name = 'ProyectoWebApp/producto_nuevo.html'

class ProductoDelete(DeleteView):
    model = Alquila
    success_url = reverse_lazy('productos')
    template_name='ProyectoWebApp/producto_confirm_delete.html'

