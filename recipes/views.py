from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    #return HTTP Response
    return render(request, 'recipes/home.html', context={
        'name': 'Lucas'
    })

def contato(request):
    return HttpResponse("CONTATO")

def sobre(request):
    return HttpResponse("SOBRE")