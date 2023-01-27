from django.http import HttpResponse
from django.shortcuts import render

def acercademi(request):
    descripcion= """Mi nombre es Francisco Alonso, tengo 26 años, resido en Cordoba Capital, Argetina. Estoy actualmente finalizando la carrera de Administracion de empresas en la Universad Blas Pascal.
    Ademas estoy capacitandome en la programacion, ya que considero que es un herramienta super util para saber manejar en el mundo de los negocios.
    Hoy 07/01/2023, estoy creando este sitio web, al cual lo realice como requisito para obtener el certificado del curso de python en la academia Coderhouse."""
    return render(request, 'Appregistros/acercademi.html', {"mensaje": descripcion})