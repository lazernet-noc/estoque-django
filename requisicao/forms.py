# flake8: noqa

from django import forms
from .models import Requisicao, ItemRequisicao
from django.core.exceptions import ValidationError

class RequisicaoForm(forms.ModelForm):

    class Meta:
        model = Requisicao
        fields = '__all__'


class ItemRequisicaoForm(forms.ModelForm):

    class Meta:
        model = ItemRequisicao
        fields = '__all__'
        
    def clean(self):
        cleaned_data = self.cleaned_data
        quantidade = cleaned_data.get('quantidade')

        if quantidade <0:
            msg = ValidationError(
                'Equipamento sem estoque',
                code='invalid'
            )
            self.add_error('quantidade', msg)

        return super().clean()

