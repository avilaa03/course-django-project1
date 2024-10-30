from django.urls import path
from recipes.views import home, sobre, contato
# HTTP Request <- HTTP Response

urlpatterns = [
    path('', home),
    path('sobre/', sobre),
    path('contato/', contato)
]