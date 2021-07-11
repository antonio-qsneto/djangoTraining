from django.http import HttpResponse, response
from django.http.request import HttpRequest
from django.shortcuts import render

def home(request):

        nome = 'antonio'

        lista = [{'nome': 'Antonio',
            'idade': '26',
            'altura': '175'}
        ]
        data = {'lista': lista, 'nome': nome}
        return render(request, 'index.html', data)

