# flake8: noqa
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse
from . import models
from django.urls import reverse
from django import forms

# Create your views here.
class ListaSaida(ListView):
    def get(self, *args, **kwargs):
        return HttpResponse('ListaSaida')



def create(request):
    form_action = reverse('saida:create')

    if request.method == 'POST':
        form = saidaForm(request.POST, request.FILES)

        context = {
            'form': form,
            'form_action': form_action,
        }

        if form.is_valid():
            saida = form
            saida.save()

            return redirect('saida:lista')

        return render(
            request,
            'saida/create.html',
            context
        )

    context = {
        'form': saidaForm(),
        'form_action': form_action,
    }

    return render(
        request,
        'saida/create.html',
        context
    )



class saidaForm(forms.ModelForm):

    class Meta:
        model = models.Saida
        fields = "__all__"