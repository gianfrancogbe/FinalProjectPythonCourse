from django.shortcuts import render, HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.views import LogoutView



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

                return render(request,'ProyectoWebApp/base.html', {'mensaje':f'Bienvenido {usuario}'})
            else:
                return render(request,'ProyectoWebApp/base.html', {'mensaje':'Por favor, intente de nuevo'})

        else:
            return render(request,'ProyectoWebApp/base.html', {'mensaje':'Error, formulario erroneo'})

    form=AuthenticationForm()

    return render(request,'ProyectoWebApp/login.html',{'form':form})
