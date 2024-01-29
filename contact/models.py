from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import os
from datetime import datetime
from django.conf import settings

def contact_picture_path(instance, filename):
    # Gere o caminho de upload com base no ID do contato
    date_str = datetime.now().strftime("%Y%m%d")
    y = datetime.now().strftime("%Y")
    m = datetime.now().strftime("%m")
    d = datetime.now().strftime("%d")
    h = datetime.now().strftime("%H")
    M = datetime.now().strftime("%M")
    s = datetime.now().strftime("%S")
    return os.path.join(f'pictures/{y}/{m}/', f'{str(instance.id)}_{d}_{h}{M}{s}_{filename}')

class MeuModelo(models.Model):
    # Seus campos de modelo aqui

    def meu_metodo(self, request):
        usuario_logado = request.user
        # Resto do código do seu método


class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length = 25)
    last_name = models.CharField(max_length = 25, blank = True)
    phone = models.CharField(max_length = 25)
    email = models.EmailField(max_length=254, blank = True)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank = True)
    show = models.BooleanField(default =True)
    # picture = models.ImageField(blank=True, upload_to=contact_picture_path)
    picture = models.ImageField(blank=True , upload_to= 'pictures/%Y/%m/')
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True, null=True
        )
    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True, null=True
        )


    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
    




    def save(self, *args, **kwargs):
        if self._state.adding:
            print('ENTROU NO SAVE')
            # Verifique se o objeto já foi salvo no banco de dados
            if not self.id:
                super().save(*args, **kwargs)
            
            if self.picture.name:
                # Crie o caminho de upload com base no ID do contato
                new_picture_path = contact_picture_path(self, os.path.basename(self.picture.name))
                media_root = settings.MEDIA_ROOT
                # Atualize o caminho da imagem para refletir o ID do contato
                old_name = f'{media_root}/{self.picture.name}'
                self.picture.name = new_picture_path
                new_picture_path = f'{media_root}/{new_picture_path}'
                print(new_picture_path)
                os.rename(old_name,new_picture_path)
                super().save(*args, **kwargs)
        else:
            old_instance = Contact.objects.get(pk=self.pk)
            super().save(*args, **kwargs)
            print('ENTROU NO UPDATE')
            
            if old_instance.picture != self.picture:
                # Crie o caminho de upload com base no ID do contato
                new_picture_path = contact_picture_path(self, os.path.basename(self.picture.name))
                media_root = settings.MEDIA_ROOT
                # Atualize o caminho da imagem para refletir o ID do contato
                old_name = f'{media_root}/{self.picture.name}'
                self.picture.name = new_picture_path
                new_picture_path = f'{media_root}/{new_picture_path}'
                print(new_picture_path)
                os.rename(old_name,new_picture_path)
                super().save(*args, **kwargs)
            