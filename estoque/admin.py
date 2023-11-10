# flake8: noqa
from django.contrib import admin
from .models import Estoque


class EstoqueAdmin(admin.ModelAdmin):
    list_display = ['nome', 'tipo', 'quantidade']
    readonly_fields = 'cadastrado', 'cadastrado_por', 'atualizado', 'atualizado_por',

    def save_model(self, request, obj, form, change):
        if change:
            obj.atualizado_por = request.user 
        else:
            obj.cadastrado_por= request.user
        obj.save()    


admin.site.register(Estoque, EstoqueAdmin)