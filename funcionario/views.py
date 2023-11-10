# flake8: noqa

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse
from . import models
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django import forms
from funcionario.models import Funcionario
from . import models

class ListaFuncionario(ListView):
    model = models.Funcionario
    template_name = 'funcionario/lista.html'
    context_object_name = 'funcionarios'



def create(request):
    form_action = reverse('funcionario:create')

    if request.method == 'POST':
        form = funcionarioForm(request.POST, request.FILES)

        context = {
            'form': form,
            'form_action': form_action,
        }

        if form.is_valid():
            funcionario = form.save()
            funcionario.save()

            return redirect('funcionario:lista')

        return render(
            request,
            'funcionario/create.html',
            context
        )

    context = {
        'form': funcionarioForm(),
        'form_action': form_action,
    }

    return render(
        request,
        'funcionario/create.html',
        context
    )
class funcionarioForm(forms.ModelForm):

    nome = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Informe o nome do Funcionário',
            }
        ),
        label='Nome',
    )
    
    cidade = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Informe a Cidade do Funcionário',
            }
        ),
        label='Cidade',
    )

    class Meta:
        model = models.Funcionario
        fields = (
            'nome', 'cidade', 
        )


def update(request, funcionario_id):
    funcionario = get_object_or_404(
        Funcionario, pk=funcionario_id,
    )
    form_action = reverse('funcionario:update', args=(funcionario_id,))

    if request.method == 'POST':
        form = funcionarioForm(request.POST, request.FILES, instance=funcionario)

        context = {
            'form': form,
            'form_action': form_action,
        }

        if form.is_valid():
            funcionario = form.save()
            funcionario.save()

            return redirect('funcionario:lista')

        return render(
            request,
            'funcionario/update.html',
            context
        )

    context = {
        'form': funcionarioForm(instance=funcionario),
        'form_action': form_action,
    }

    return render(
        request,
        'funcionario/update.html',
        context
    )

    
def delete(request, funcionario_id):
    funcionario = get_object_or_404(
        Funcionario, pk=funcionario_id,
    )

    if request.method == 'POST':
        funcionario.delete()
        return redirect('funcionario:lista')

    return render(
        request,
        'funcionario/delete.html',
                {
            'funcionario': funcionario,
            
        }
    )
