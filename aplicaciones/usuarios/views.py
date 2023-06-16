from pyexpat.errors import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

#Clases para las plantillas
from django.views.generic import View,TemplateView, CreateView, UpdateView, DetailView, ListView, DeleteView

from aplicaciones.usuarios.form import NewUserForm

# Create your views here.

class Perfil_Usuario(TemplateView):

    template_name = "usuarios/perfil-usuario.html"

    def dispatch(self, request, *args, **kwargs):

        if request.user.is_anonymous:
            print("No estas autenticado, eres un usuario anonimo")
            return redirect("login:login")

        else:

            print("Estas autenticado GENIAL")
            #print("usuario permisos: ",request.user.get_all_permissions())
            #Aqui verificamos si el usuario esta activo para que ingrese
            ''' 
            if request.user.activo:   
                print("Usuario activo y validado")
            else:
                print("El usuario no esta activo")
                messages.add_message(request, messages.INFO, "Usuario Inactivo")
                return redirect("src:logout")
            '''


        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):


        context = super().get_context_data(**kwargs)
        #context['informacion'] = "Hola..."

       
        context['usuario'] = self.request.user
        #context['contrato'] = Contrato.objects.get(usuario=self.request.user)
        context['contrato'] = "Sin contrato"
        print("en contextos:",context['contrato'])
        return context

 
def registrarUsuario(request):  

    if request.POST == 'POST':  
        form = NewUserForm()  
        if form.is_valid():  
            form.save()  
            messages.success(request, 'Account created successfully')  
  
    else:  
        form = NewUserForm()  
    context = {  
        'form':form  
    }  
    return render(request, 'usuarios/registrar-usuario.html', context)