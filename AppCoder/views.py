from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Curso

def curso(self):

    curso1=Curso(nombre="Python", camada="27615")

    curso1.save()

    documento = f"Tu curso es {curso1.nombre} y tu camada es {curso1.camada}"

    return HttpResponse(documento)