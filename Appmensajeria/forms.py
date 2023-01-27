from django import forms
from django.contrib.auth.models import User
import datetime

class Mensajeform(forms.Form):
    destinatario=forms.CharField(label="destinatario", max_length=20)
    asunto=forms.CharField(label="asunto", max_length=90)
    cuerpo=forms.CharField(label="cuerpo", max_length=500)
    autor=User.username
    fecha=datetime.datetime.now()
