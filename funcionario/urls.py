# flake8: noqa
from django.urls import path
from . import views

app_name = 'funcionario'

urlpatterns = [
    path('', views.ListaFuncionario.as_view(), name='lista'),
    path('create/', views.create, name='create'),
    path('update/<int:funcionario_id>/', views.update, name='update'),
    path('delete/<int:funcionario_id>/', views.delete, name='delete'),
]
