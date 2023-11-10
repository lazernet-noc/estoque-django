# flake8: noqa
from django.db import models
from funcionario.models import Funcionario 
from estoque.models import Estoque


class Requisicao(models.Model):
    funcionario = models.ForeignKey(Funcionario, verbose_name='Funcionário', on_delete=models.SET_NULL,null=True)
    data = models.DateTimeField(auto_now_add=True)
    observacao = models.CharField(max_length=500, blank=True, null=True, verbose_name='Observações')

    def __str__(self):
        return f'Requisição N. {self.pk}'
    
    class Meta:
        verbose_name = 'Requisição'
        verbose_name_plural = 'Requisições'
    
class ItemRequisicao(models.Model):
    requisicao = models.ForeignKey(Requisicao, on_delete=models.CASCADE)
    equipamento = models.ForeignKey(Estoque, verbose_name='Equipamento', on_delete=models.SET_NULL,null=True)

    quantidade = models.PositiveIntegerField()


    def __str__(self):
        return f'Item da {self.requisicao}'
    
    class Meta:
        verbose_name = 'Item da Requisição'
        verbose_name_plural = 'Itens da Requisição'


