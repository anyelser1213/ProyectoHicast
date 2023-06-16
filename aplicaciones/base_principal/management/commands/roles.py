from django.core.management.base import BaseCommand, CommandError

#Aqui esta el modelo de los roles
from aplicaciones.usuarios.models import Roles

class Command(BaseCommand):
    help = 'comando para crear los roles'

    def handle(self, *args, **options):


        print("VAMOS A CREAR LOS ROLES")
        #Creamos todos los grupos a usar
        Rol_master= Roles.objects.create(nombre="master") #Rol para master
        #Este usuario es quien vera todo incluyendo las congregaciones(sucursales)

        Rol_administrador = Roles.objects.create(nombre="administrador") #Rol para administrador
        #Este usuario se encargara de la administracion del sistema de su congregacion


        Rol_apostol = Roles.objects.create(nombre="apostol") #Rol para apostol
        Rol_prebistero = Roles.objects.create(nombre="prebistero") #Rol para prebisteros
        Rol_profeta = Roles.objects.create(nombre="profeta") #Rol para profeta

        #solo seran 2 pastores congregacionales en cada congregacion(sucursal)
        Rol_pastor_congregacional = Roles.objects.create(nombre="pastor_congregacional") #Rol para pastor
        #Maximo 24 pastores base
        Rol_pastor_base = Roles.objects.create(nombre="pastor_base") #Rol para pastor
        #Ilimitado
        Rol_pastor = Roles.objects.create(nombre="pastor") #Rol para pastor
        #Ilimitado
        Rol_lider = Roles.objects.create(nombre="lider") #Rol para lider
        #Ilimitado
        Rol_creyente = Roles.objects.create(nombre="creyente") #Rol para creyente
         
        self.stdout.write(self.style.HTTP_SUCCESS("ROLES CREADOS CON EXITO"))
        #self.stdout.write(self.style.WARNING("Texto de advertencia"))