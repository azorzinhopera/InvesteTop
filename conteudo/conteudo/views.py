from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def carteira(request):
    x = 'ola'
    return render(request, 'carteira.html', {'ola':x})

def informacao(request):
    return render(request, 'informacao.html')

def melhores(request):
    return render(request, 'melhores.html')