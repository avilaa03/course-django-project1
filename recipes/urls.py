from django.urls import path
from . import views
# HTTP Request <- HTTP Response

urlpatterns = [
    path('', views.home),
    path('recipes/<int:id>/', views.recipe),
]