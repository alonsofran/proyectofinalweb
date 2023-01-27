from django.urls import path
from Appmensajeria.views import *

urlpatterns = [
path("mensaje/", mensaje, name="mensaje"),
path("mostrarmensaje/", mostrarmensaje, name="mostrarmensaje"),
]