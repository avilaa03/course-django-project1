from django.shortcuts import render

def home(request):
    #return HTTP Response
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Lucas'
    })

def recipe(request, id):
    #return HTTP Response
    return render(request, 'recipes/pages/recipe-view.html', context={
        'name': 'Lucas'
    })
