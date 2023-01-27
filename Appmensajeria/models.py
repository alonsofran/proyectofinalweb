from django.db import models

# Create your models here.

class Mensaje(models.Model):
    asunto=models.CharField(max_length=90)
    cuerpo=models.CharField(max_length=500)
    autor=models.CharField(max_length=20)
    fecha=models.DateField()
    destinatario=models.CharField(max_length=20)