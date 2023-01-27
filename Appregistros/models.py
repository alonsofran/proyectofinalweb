from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Usuarios(models.Model):
    usuario=models.CharField(max_length=20)
    clave=models.CharField(max_length=20)
    email=models.EmailField()

    def __str__(self):
        return self.usuario

class Blog(models.Model):
    titulo=models.CharField(max_length=60)
    subtitulo=models.CharField(max_length=60)
    cuerpo=models.CharField(max_length=500)
    autor=models.CharField(max_length=20)
    fecha=models.DateField()
    imagen=models.ImageField(upload_to="imagen")
    


    def __str__(self):
        return f"{self.titulo} - {self.subtitulo} / {self.autor}"

class Imagenblog(models.Model):
    imagen= models.ImageField(upload_to="imagenblog")
    blog=models.ForeignKey(Blog, on_delete=models.CASCADE)