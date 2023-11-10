# flake8: noqa
from django.urls import path
from . import views

app_name = 'estoque'

urlpatterns = [
    path('', views.ListaEstoque.as_view(),name="lista"),
    path('create/', views.create, name='create'),
    path('detail/<int:estoque_id>/', views.detail, name='detail'),
    path('update/<int:estoque_id>/', views.update, name='update'),
    path('delete/<int:estoque_id>/', views.delete, name='delete'),
    path('search/', views.search, name='search'),

]
