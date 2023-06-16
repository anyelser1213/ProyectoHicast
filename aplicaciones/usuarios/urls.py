from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views as VistasUsuario

app_name ="usuarios"

urlpatterns = [


    path('perfil', VistasUsuario.Perfil_Usuario.as_view(), name='perfil'),
    path('registrarPaciente', VistasUsuario.registrarUsuarioPaciente, name='registrarUsuarioPaciente'),
    path('registrarProfesional', VistasUsuario.registrarUsuarioProfesional, name='registrarUsuarioProfesional'),
    path('registrarUsuario', VistasUsuario.registrarUsuario, name='registrarUsuario'),
    path('listar usuarios', VistasUsuario.UsuariosListView.as_view(), name='listaUsuarios'),
    #path('login/', vistasLogin.Login.as_view() ,name="login"),
    
    #path('', views.index.as_view() ,name="index"),



    
    
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)