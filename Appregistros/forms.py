from django import forms

from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User


class Blogform(forms.Form):
    titulo=forms.CharField(label="Titulo", max_length=60)
    subtitulo=forms.CharField(label="Subtitulo", max_length=60)
    cuerpo=forms.CharField(label="Cuerpo del blog", max_length=500)
    autor=User.username
    fecha=forms.DateField(label="Fecha")
    imagen=forms.ImageField(label="imagen")

class Blogforms(forms.Form):
    titulo=forms.CharField(label="Titulo", max_length=60)
    subtitulo=forms.CharField(label="Subtitulo", max_length=60)
    cuerpo=forms.CharField(label="Cuerpo del blog", max_length=500)
    autor=User.username
    fecha=forms.DateField(label="Fecha")

class RegistroUsuarioForm(UserCreationForm):

    email= forms.EmailField(label="Email")
    password1= forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model=User
        fields=["username", "email", "password1", "password2"]
        help_texts = {k:"" for k in fields}#para cada uno de los campos del formulario, le asigna un valor vacio

class EditarUsuarioForm(UserCreationForm):

    password1= forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)
    first_name=forms.CharField(label="ingrese el nombre", max_length= 20)
    last_name=forms.CharField(label="ingrese su apellido", max_length= 20)
    email= forms.EmailField(label="Email")

    class Meta:
        model=User
        fields=["email", "password1", "password2", "first_name", "last_name"]
        help_texts = {k:"" for k in fields}#para cada uno de los campos del formulario, le asigna un valor vacio
