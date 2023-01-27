from django.shortcuts import render

from Appmensajeria.forms import *
from Appmensajeria.models import *
import datetime


from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def mensaje(request):
    if request.method=="POST":
        form=Mensajeform(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            asunto=informacion["asunto"]
            cuerpo=informacion["cuerpo"]
            autor=request.user
            fecha=datetime.datetime.now()
            destinatario=informacion["destinatario"]
            mensaje=Mensaje(asunto=asunto, cuerpo=cuerpo, autor=autor, fecha=fecha, destinatario=destinatario)
            mensaje.save()
            return render(request, "Appregistros/inicio.html", {"notificacion":"mensaje enviado"})
        else:
            return render(request, "Appregistros/inicio.html", {"notificacion":"Informacion no valida"})
    else:
        miformulario=Mensajeform()
        return render(request, "Appregistros/mensaje.html", {"form":miformulario})

@login_required
def mostrarmensaje(request):
    usuario=request.user
    mensajes=Mensaje.objects.filter(destinatario=request.user)
    return render(request, "Appregistros/mostrarmensaje.html", {"mensajes":mensajes})






