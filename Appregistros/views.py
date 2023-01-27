from django.shortcuts import render
from Appregistros.forms import *
from Appregistros.models import *

from django.contrib.auth.forms import  UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate

from django.contrib.auth.decorators import login_required



# Create your views here.

def inicio(request):
    return render(request, "Appregistros/inicio.html")

"""def usuarioformulario(request):
    if request.method=='POST':
        form=Usuarioform(request.POST)

        if form.is_valid():
            informacion=form.cleaned_data
            usuario=informacion["usuario"]
            clave=informacion["clave"]
            email=informacion["email"]
            usuario1=Usuarios(usuario=usuario, clave=clave, email=email)
            usuario1.save()
            return render(request, 'Appregistros/inicio.html', {"mensaje":"usuario cargado"})
        else:
            return render(request, 'Appregistros/usuarioformulario.html', {"form":form, "mensaje":"informacion no valida"})
    else:
        formulario=Usuarioform()
        return render(request, "Appregistros/usuarioformulario.html", {"form":formulario})"""


def mostrarblogs(request):
    blogs=Blog.objects.all()
    return render(request, "Appregistros/mostrarblogs.html",{"blogs":blogs})

def verblog(request, id):
    blog=Blog.objects.get(id=id)
    return render(request, "Appregistros/verblog.html", {"blog":blog})

@login_required
def blogformulario(request):
    if request.method=="POST":
        form= Blogform(request.POST, request.FILES)
        if form.is_valid():
            informacion=form.cleaned_data
            titulo= informacion["titulo"]
            subtitulo= informacion["subtitulo"]
            cuerpo= informacion["cuerpo"]
            autor= request.user
            fecha= informacion["fecha"]
            imagen=request.FILES["imagen"]
            blog1= Blog(titulo=titulo, subtitulo=subtitulo, cuerpo=cuerpo, autor=autor, fecha=fecha, imagen=imagen)
            blog1.save()
            blogs=Blog.objects.all()
            return render(request, "Appregistros/mostrarblogs.html", {"blogs":blogs, "mensaje": "Blog cargado"})
        else:
            return render(request, "Appregistros/blogformulario.html" ,{"form": form, "mensaje": "Informacion no valida"})
    else:
        formulario= Blogform()
        return render (request, "Appregistros/blogformulario.html", {"form": formulario})

@login_required
def editarblog(request, id):
    blog=Blog.objects.get(id=id)
    if request.method=="POST":
        formulario=Blogforms(request.POST)
        if formulario.is_valid():
            info=formulario.cleaned_data
            blog.titulo=info["titulo"]
            blog.subtitulo=info["subtitulo"]
            blog.cuerpo=info["cuerpo"]
            blog.fecha=info["fecha"]
            blog.save()
            return render(request, "Appregistros/inicio.html" ,{"mensaje": "blog editado correctamente"})
        pass
    else:
        formulario= Blogforms(initial={"titulo":blog.titulo, "subtitulo":blog.subtitulo, "cuerpo":blog.cuerpo, "autor":blog.autor, "fecha":blog.fecha})
        return render(request, "Appregistros/editarblog.html", {"forms": formulario, "blog": blog})

@login_required
def eliminarblog(request, id):
    blog=Blog.objects.get(id=id)
    blog.delete()
    return render(request, "Appregistros/inicio.html", {"mensaje": "Blog eliminado correctamente"})

def busquedablog(request):
    return render(request, "Appregistros/busquedablog.html")

def buscar(request):
    blog= request.GET["titulo"]
    if blog!="":
        blogs= Blog.objects.filter(titulo__icontains=blog)
        return render(request, "Appregistros/resultadosbusquedablog.html", {"blogs": blogs, "blog":blog})
    else:
        return render(request, "Appregistros/busquedablogs.html", {"mensaje": "Porfavor ingresa un titulo para buscar!"})


def register(request):
    if request.method=="POST":
        form= RegistroUsuarioForm(request.POST)
        if form.is_valid():
            username= form.cleaned_data.get("username")
            form.save()
            return render(request, "Appregistros/inicio.html", {"mensaje":f"Usuario {username} creado correctamente"})
        else:
            return render(request, "Appregistros/register.html", {"form": form, "mensaje":"Error al crear el usuario"})
    else:
        form= RegistroUsuarioForm()
        return render(request, "Appregistros/register.html", {"form": form})

def login_request(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usu=info["username"]
            clave=info["password"]
            usuario=authenticate(username=usu, password=clave)#verifica si el usuario existe, si existe, lo devuelve, y si no devuelve None 
            if usuario is not None:
                login(request, usuario)
                return render(request, "Appregistros/inicio.html", {"mensaje":f"Usuario {usu} logueado correctamente"})
            else:
                return render(request, "Appregistros/login.html", {"form": form, "mensaje":"Usuario o contraseña incorrectos"})
        else:
            return render(request, "Appregistros/login.html", {"form": form, "mensaje":"Usuario o contraseña incorrectos"})
    else:
        form=AuthenticationForm()
        return render(request, "Appregistros/login.html", {"form": form})

@login_required
def editarperfil(request):
    usuario=request.user
    blogs=Blog.objects.filter(autor=request.user)
    if request.method=="POST":
        form=EditarUsuarioForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usuario.password1=info["password1"]
            usuario.password2=info["password2"]
            usuario.first_name=info["first_name"]
            usuario.last_name=info["last_name"]
            usuario.set_password(str(usuario.password1))
            usuario.save()
            return render(request, "Appregistros/inicio.html", {"mensaje": f"Usuario {usuario.username} modificado"})
        else:
            return render(request, "Appregistros/editarperfil.html", {"form":form, "mensaje":"no se pudo modificar el usuario"})
    else:
        form=EditarUsuarioForm(instance=usuario)
        return render(request, "Appregistros/editarperfil.html", {"form":form, "nombreusuario":usuario.username, "blogs":blogs})


#NO SE COMO TRAER EN LA VARIABLE BLOG EL BLOG DEL USUARIO LOGEADO


