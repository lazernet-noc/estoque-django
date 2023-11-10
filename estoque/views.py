# flake8: noqa
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse
from . import models
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django import forms
from estoque.models import Estoque
from django.db.models import Q
# Create your views here.

class ListaEstoque(ListView):
    model = models.Estoque
    template_name = 'estoque/lista.html'
    context_object_name = 'estoques'


def create(request):
    form_action = reverse('estoque:create')

    if request.method == 'POST':
        form = estoqueForm(request.POST, request.FILES)

        context = {
            'form': form,
            'form_action': form_action,
        }

        if form.is_valid():
            estoque = form.save()
            estoque.save()

            return redirect('estoque:lista')

        return render(
            request,
            'estoque/create.html',
            context
        )

    context = {
        'form': estoqueForm(),
        'form_action': form_action,
    }

    return render(
        request,
        'estoque/create.html',
        context
    )

def detail(request, estoque_id):
   
    # single_Estoque = Estoque.objects.filter(pk=estoque_id).first()
    single_estoque = get_object_or_404(
        Estoque, pk=estoque_id,
    )
    
    context = {
        'estoque': single_estoque,
    
    }

    return render(
        request,
        'estoque/detail.html',
        context
    )

def update(request, estoque_id):
    estoque = get_object_or_404(
        Estoque, pk=estoque_id,
    )
    form_action = reverse('estoque:update', args=(estoque_id,))

    if request.method == 'POST':
        form = estoqueForm(request.POST, request.FILES, instance=estoque)

        context = {
            'form': form,
            'form_action': form_action,
        }

        if form.is_valid():
            estoque = form.save()
            estoque.save()

            return redirect('estoque:detail', estoque_id=estoque.pk)

        return render(
            request,
            'estoque/update.html',
            context
        )

    context = {
        'form': estoqueForm(instance=estoque),
        'form_action': form_action,
    }

    return render(
        request,
        'estoque/update.html',
        context
    )

    
def delete(request, estoque_id):
    estoque = get_object_or_404(
        Estoque, pk=estoque_id,
    )

    if request.method == 'POST':
        estoque.delete()
        return redirect('estoque:lista')

    return render(
        request,
        'estoque/delete.html',
                {
            'estoque': estoque,
            
        }
    )

class estoqueForm(forms.ModelForm):
    imagem = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept': 'image/*',
            }
        ),
        required=False
    )
    nome = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Informe o nome do equipamento',
            }
        ),
        label='Equipamento',
    )



    class Meta:
        model = models.Estoque
        fields = (
            'nome', 'tipo', 'quantidade',
            'imagem', 
        )

def search(request):
    search_value = request.GET.get('q', '').strip()

    if search_value == '':
        return redirect('estoque:lista')

    estoques = Estoque.objects \
        .filter(
            Q(nome__icontains=search_value)  
            )

    context = {
        'estoques' : estoques,
       
    }

    return render(
        request,
        'estoque/lista.html',
        context
    )
