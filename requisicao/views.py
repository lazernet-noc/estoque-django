from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from .models import Requisicao, ItemRequisicao
from django.forms import inlineformset_factory
from .forms import RequisicaoForm, ItemRequisicaoForm


class ListaRequisicao(View):

    def get(self, *args, **kwargs):
        return HttpResponse('ListaRequisicao')


class Criar(View):

    def get(self, *args, **kwargs):
        return HttpResponse('Criar')


class Atualizar(View):

    def get(self, *args, **kwargs):
        return HttpResponse('Atualizar')


class Deletar(View):

    def get(self, *args, **kwargs):
        return HttpResponse('Deletar')


def estoque_entrada_add(request):
    template_name = 'estoque_entrada_form.html'
    requisicao_form = Requisicao()
    item_requisicao_formset = inlineformset_factory(
        Requisicao,
        ItemRequisicao,
        form=ItemRequisicaoForm,
        extra=0,
        min_num=1,
        validate_min=True,
    )
    if request.method == 'POST':
        form = RequisicaoForm(request.POST, instance=requisicao_form, prefix='main')
        formset = item_requisicao_formset(
            request.POST,
            instance=requisicao_form,
            prefix='estoque'
        )
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()

            return redirect('estoque:lista')
    else:
        form = RequisicaoForm(instance=requisicao_form, prefix='main')
        formset = item_requisicao_formset(instance=requisicao_form, prefix='estoque')
    context = {'form': form, 'formset': formset}
    return render(request, template_name, context)
