# flake8: noqa
from django.urls import path
from . import views

app_name = 'saida'

urlpatterns = [
    path('', views.ListaSaida.as_view(), name='lista'),
    path('create/', views.create, name='create'),
]
