from django.core.management.base import BaseCommand, CommandError

#Estos dos modelos son para crear permisos personalizados
from django.contrib.auth.models import Permission,Group

#Aqui estan los ministerios
from aplicaciones.ministerios.models import Ministerios


class Command(BaseCommand):
    help = 'comando para crear los grupos'

    def handle(self, *args, **options):


        print("VAMOS A CREAR LOS GRUPOS...")

        #Creamos todos los grupos a usar
        Grupo_master= Group.objects.create(name="master") #Permisos solo para master
        Grupo_administrador= Group.objects.create(name="administrador") #Permisos para administrador
        Grupo_apostol = Group.objects.create(name="apostol")
        Grupo_prebistero = Group.objects.create(name="prebistero") #Permisos solo para prebisteros
        Grupo_profeta = Group.objects.create(name="profeta") #Permisos solo para profetas
        Grupo_pastor_congregacional = Group.objects.create(name="pastor congregacional") #Permisos solo para pastor base
        Grupo_pastor_base = Group.objects.create(name="pastor base") #Permisos solo para pastor base
        Grupo_pastor = Group.objects.create(name="pastor") #Permisos solo para pastor
        Grupo_lider = Group.objects.create(name="lider") #Permisos solo para lider
        Grupo_creyente = Group.objects.create(name="creyente") #Permisos solo para creyentes
            
            
        #Grupo_master.permissions.set(list(Permission.objects.all())) #Todos los permisos para usuario master
        #Grupo_apostol.permissions.set(list(Permission.objects.all())) #Todos los permisos para usuario master
        #Grupo_prebistero.permissions.set(list(Permission.objects.all())) #Todos los permisos para usuario master
        #Grupo_profeta.permissions.set(list(Permission.objects.all())) #Todos los permisos para usuario master


        #Grupo_productor.permissions.add(
            #                    Permission.objects.get(name="Can add inventario"),
            #                    Permission.objects.get(name="Can change inventario"),
            #                    Permission.objects.get(name="Can delete inventario"),
            #                    Permission.objects.get(name="Can view inventario"),
            #                    Permission.objects.get(name="Can add producto"),
            #                    Permission.objects.get(name="Can change producto"),
            #                    Permission.objects.get(name="Can delete producto"),
            #                    Permission.objects.get(name="Can view producto"),
            #)
            #Grupo_cliente.permissions.add(
            #                    Permission.objects.get(name="peticiones"),
            #)
            

            #Luego editamos los permisos que corresponden a cada uno
            #Grupo_pastor.permissions.set(list(Permission.objects.all())) #Todos los permisos para usuario master
            #Grupo_lider.permissions.set(list(Permission.objects.all())) #Todos los permisos para usuario master
            #Grupo_administrador.permissions.add(permiso1, permiso2, ...)
            #self.groups.add(Grupo_administrador)

            #migrupo = Group.objects.get(name="master")
         
        self.stdout.write(self.style.HTTP_SUCCESS("GRUPOS CREADOS CON EXITO"))
        #self.stdout.write(self.style.WARNING("Texto de advertencia"))