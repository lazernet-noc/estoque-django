# flake8: noqa
from django.urls import path
from . import views

app_name = 'requisicao'

urlpatterns = [
    path('', views.ListaRequisicao.as_view(), name='lista'),
    path('add/', views.estoque_entrada_add, name='estoque_entrada_add'),
    path('atualizar/', views.Atualizar.as_view(), name='atualizar'),
    path('deletar/', views.Deletar.as_view(), name='deletar'),
]