# flake8: noqa
from django.db import models

class Funcionario(models.Model):
    nome = models.CharField(max_length=255, verbose_name='Nome do Funcinário')
    cidade = models.CharField(max_length=255, verbose_name='Cidade')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'
