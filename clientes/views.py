from django.http import HttpResponse
from django.http.request import HttpRequest
from django.shortcuts import render


def clientes(request):
    return HttpResponse("Joao, Eduardo, Jessica")

def clienteDetalhe(requeste, id):
    return HttpResponse(id)

def clienteNome(request, nome):
    return HttpResponse("Ola %s" % nome)
