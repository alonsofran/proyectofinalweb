from django.urls import path
from Appregistros.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
path("", inicio, name="inicio"),
path("mostrarblogs/", mostrarblogs, name="mostrarblogs"),
path("verblog/<id>", verblog, name="verblog"),
path("blogformulario/", blogformulario, name="blogformulario"),
path("editarblog/<id>", editarblog, name="editarblog"),
path("eliminarblog/<id>", eliminarblog, name="eliminarblog"),
path("busquedablog/", busquedablog, name="busquedablog"),
path("buscar/", buscar, name="buscar"),

path("register/", register, name="register"),
path("login/", login_request, name="login"),
path('logout/', LogoutView.as_view(), name='logout'),
path('editarperfil/', editarperfil, name="editarperfil"),
]