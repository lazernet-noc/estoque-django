# flake8: noqa
from django.db import models
from PIL import Image
from django.contrib.auth.models import User
from pathlib import Path
from django.conf import settings

# Create your models here.
class Estoque(models.Model):
    nome = models.CharField(max_length=255, verbose_name='Nome do Equipamento')
    tipo = models.CharField(
        max_length=25,
        default='Roteador',
        choices= (
            ('Roteador','Roteador'),
            ('ONU','ONU'),
            ('Conector','Conector'),
            ('Cabo','Cabos'),
            ('Outros','Outros'),
        )
    )
    quantidade = models.PositiveBigIntegerField(default=1)
    imagem = models.ImageField(upload_to='equipamento_imagens', blank=True, null= True)
    mac = models.CharField(max_length=17, verbose_name='Mac do Equipamento',blank=True, null=True)
    cadastrado = models.DateTimeField(auto_now_add=True)
    # user.post_created_by.all
    cadastrado_por = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True, null=True,
        verbose_name='Cadastrado por: ',
        related_name='estoque_cadastro_por'
    )
    atualizado = models.DateTimeField(auto_now=True)
    # user.post_updated_by.all
    atualizado_por = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True, null=True,
        verbose_name ='Atualizado por: ',
        related_name='estoque_atualizado_por'
    )

    def __str__(self):
        return self.nome
    
    @staticmethod
    def resize_image(img, new_width=200):
        img_full_path = Path(settings.MEDIA_ROOT, img.name)
        img_pil = Image.open(img_full_path)
        original_width, original_height = img_pil.size
                   
        if original_width <= new_width:               
            img_pil.close()
            return

        new_height = 200

        new_img = img_pil.resize((new_width, new_height), Image.LANCZOS)
        new_img.save(
            img_full_path,
            optimize=True,
            quality=50
            )

    def save (self, *args, **kwargs):
        super().save(*args, **kwargs)
        max_image_size = 200

        if self.imagem:
            self.resize_image(self.imagem, max_image_size)
           
    
    class Meta:
          verbose_name = 'Estoque'
          verbose_name_plural = 'Estoque'