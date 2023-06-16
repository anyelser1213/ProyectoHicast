
from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
#Estos dos modelos son para crear permisos personalizados
from django.contrib.auth.models import Permission,Group



#Clases para las plantillas
from django.views.generic import TemplateView, CreateView, UpdateView, DetailView, ListView, DeleteView

#Para las fechas
from datetime import datetime





class Index(TemplateView):

    #Esta en base_principal
    #template_name = "index.html"
    template_name = "index-hicast.html"

    def dispatch(self, request, *args, **kwargs):

        if request.user.is_anonymous:
            print("No estas autenticado, eres un usuario anonimo")
            return redirect("login:login")

        else:

            print("Estas autenticado GENIAL")
            #print("Permisos: ",list(Permission.objects.all()))
            print("usuario: ",request.user," Cantidad de Grupos: ",Group.objects.all().count())

            #GCliente = Group.objects.get(name="cliente_E")

            print("\n\n")
            #print("\n\nPermisos Grupo Productor: ",GProductor.permissions.all() )
            #for elemento in GCliente.permissions.all():
            #    print(elemento.name)
            #print("\n\n")

            #Grupo_productor.permissions.set(Permission.objects.get(name="Can add inventario"),
            print("administrador:",request.user.groups.filter(name='administrador').exists())
            print("productor:",request.user.groups.filter(name='productor').exists())
            print("cliente :",request.user.groups.filter(name='cliente').exists())
            print("\n\n")
            



        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['informacion'] = "Hola..."


        return context




