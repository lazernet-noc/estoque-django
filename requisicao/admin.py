# flake8: noqa
from django.contrib import admin
from . import models

class ItemRequisicaoInline(admin.TabularInline):
    model = models.ItemRequisicao
    extra = 0

class RequisicaoAdmin(admin.ModelAdmin):
    inlines = [
        ItemRequisicaoInline
    ]    


admin.site.register(models.Requisicao, RequisicaoAdmin)
admin.site.register(models.ItemRequisicao)
