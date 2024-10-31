from django.urls import path
from recipes.views import home
# HTTP Request <- HTTP Response

urlpatterns = [
    path('', home),
]