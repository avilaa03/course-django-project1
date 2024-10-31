from django.shortcuts import render

def home(request):
    #return HTTP Response
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Lucas'
    })