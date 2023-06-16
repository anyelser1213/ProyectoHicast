from django import forms
from django.contrib import admin
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.exceptions import ValidationError
from django.db.models import fields
from django.forms import ClearableFileInput, ModelForm, widgets
from aplicaciones.usuarios.models import Usuarios



###################### AQUI COMIENZAN LOS FORMULARIOS PARA TODO DE INVENTARIO ##########################################
'''
class CalidadForm(ModelForm):


    def __init__(self, *args, **kwargs):
        #usuario_id = kwargs.pop('usuario')
        #self.usuarioID = kwargs.pop('user')
        super(CalidadForm, self).__init__(*args, **kwargs)
        print("Formulario CalidadForm: \n")
        #print("usuario: ",self.usuarioID)
        #print("usuario ID: ",self.usuarioID.id)

        #self.fields['creado_por'].empty_label = None
        #self.fields['creado_por'].queryset = Usuarios.objects.filter(id=self.usuarioID.id)

        #self.fields['imagen'].widget.attrs.update({'class': 'form-control ' })

    class Meta:

        model = Calidad
        fields = "__all__"
        widgets = {
            "nombre": forms.TextInput(attrs={'class': 'form-control','placeholder':'Ingresa nombre de calidad'}),
            #"direccion": forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter company address'}),
            #"descripcion": forms.Textarea(attrs={'class': 'form-control border-input','rows':'3','placeholder':'Enter company information'}),
            #"sitio_web": forms.TextInput(attrs={'class': 'form-control border-input','rows':'3','placeholder':'Enter website'}),
            #"color": forms.TextInput(attrs={'type': 'color', 'class':'form-control oculto2'}),
            #"imagenEmpresa": forms.ImageField(attrs={'class': 'form-control','placeholder':'Enter department image'}),
            #"imagenEmpresa":forms.ClearableFileInput(attrs={'class': 'form-control oculto','placeholder':'Enter company image'}),
            #"videoEmpresa": forms.ClearableFileInput(attrs={'class': 'form-control oculto','placeholder':'Enter company video','accept':'video/*'}),
            #"creado_por": forms.Select(attrs={'class': 'form-select','style': 'display:none'  }),
        }


'''

class UsuarioPacienteForm(UserCreationForm):

    
    def __init__(self, *args, **kwargs):
        #usuario_id = kwargs.pop('usuario')
        super(UsuarioPacienteForm, self).__init__(*args, **kwargs)
        print("Formulario UsuarioPacienteForm")
        #self.fields['rol'].empty_label = True
        self.fields["rol"].choices = [("paciente", "Paciente"),]

    class Meta:
        model = Usuarios
        #fields = '__all__'
        exclude = ('user_permissions','groups','last_login','activo','admin','is_superuser','imagenPerfil','password')

        widgets = {
            "nombre": forms.TextInput(attrs={'class': 'form-control','placeholder':'Ingresa nombre de calidad'}),
            'rol': forms.Select(attrs={'hidden': True,}),
            #"direccion": forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter company address'}),
            #"descripcion": forms.Textarea(attrs={'class': 'form-control border-input','rows':'3','placeholder':'Enter company information'}),
            #"sitio_web": forms.TextInput(attrs={'class': 'form-control border-input','rows':'3','placeholder':'Enter website'}),
            #"color": forms.TextInput(attrs={'type': 'color', 'class':'form-control oculto2'}),
            #"imagenEmpresa": forms.ImageField(attrs={'class': 'form-control','placeholder':'Enter department image'}),
            #"imagenEmpresa":forms.ClearableFileInput(attrs={'class': 'form-control oculto','placeholder':'Enter company image'}),
            #"videoEmpresa": forms.ClearableFileInput(attrs={'class': 'form-control oculto','placeholder':'Enter company video','accept':'video/*'}),
            #"creado_por": forms.Select(attrs={'class': 'form-select','style': 'display:none'  }),
        }