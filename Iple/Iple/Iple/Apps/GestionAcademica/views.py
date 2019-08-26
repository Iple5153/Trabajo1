from django.shortcuts import render
from django.http import HttpResponse
# Crear las vistas aqui
def Indice(request):
	return HttpResponse("INDICE")


