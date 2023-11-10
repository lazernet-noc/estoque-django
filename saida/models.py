# flake8: noqa
from django.db import models
from funcionario.models import Funcionario 
from estoque.models import Estoque


class Saida(models.Model):
    funcionario = models.ForeignKey(Funcionario, verbose_name='Funcionário', on_delete=models.SET_NULL,null=True)
    data = models.DateTimeField(auto_now_add=True)
    observacao = models.CharField(max_length=500, blank=True, null=True, verbose_name='Observações')
    equipamento = models.ForeignKey(Estoque, verbose_name='Equipamento', on_delete=models.SET_NULL,null=True)
    quantidade_saida = models.PositiveIntegerField()

    def __str__(self):
        return f'Retirada N. {self.pk}'
    
    class Meta:
        verbose_name = 'Saida estoque'
        verbose_name_plural = 'Saida estoque'
    