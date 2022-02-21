from django.urls import path
from ProyectoWebApp.views import inicio
from django.conf import settings
from django.conf.urls.static import static
from .views import login_request, LogoutView



urlpatterns = [
    
    path("", inicio, name="inicio"),
    path("login", login_request,name = 'Login'),
    path("logout", LogoutView.as_view(template_name = "ProyectoWebApp/logout.html"), name = "Logout")
    
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

