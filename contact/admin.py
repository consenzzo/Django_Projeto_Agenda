from django.contrib import admin
from contact import models
from datetime import datetime
from django.core.files.storage import default_storage
import os
from django.core.files.base import ContentFile

# Register your models here.
@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id','first_name','last_name', 'phone','show',
    ordering = '-id', #Sinal negativa para listar em ordem decrescente
    # list_filter = 'created_date',
    search_fields = 'id', 'first_name' , 'last_name',
    list_per_page = 25
    list_max_show_all = 100
    list_editable = 'phone','show',
    list_display_links = 'id', 'first_name', 


    # def save_model(self, request, obj, form, change):

        # super().save_model(request, obj, form, change)
        
        # if 'picture' in request.FILES:
        #     new_picture = request.FILES['picture']
        #     original_file_name = new_picture.name
        #     print('ENTROOOOOOOOOOOOOOOOOOOOOU')
        #     # Criar novo nome de arquivo
        #     date_str = datetime.now().strftime("%Y%m%d")
        #     y = datetime.now().strftime("%Y")
        #     m = datetime.now().strftime("%m")
        #     d = datetime.now().strftime("%d")
        #     file_name = os.path.basename(original_file_name)
        #     new_file_name = f'pictures/{y}/{m}/{d}_{obj.id}_{file_name}'
        #     print(f'new_file_name = {new_file_name}')

        #     # Copiar o arquivo para o novo nome
        #     # if default_storage.exists(original_file_name):
        #     #     file_content = default_storage.open(original_file_name).read()
        #     #     default_storage.save(new_file_name, ContentFile(file_content))

        #     #     # Atualizar o campo 'picture' no modelo Contact
        #     #     contact.picture.name = new_file_name
        #     #     contact.save()

        #     #     # Excluir o arquivo antigo
        #     #     default_storage.delete(original_file_name)
        #     #     print(f'É ESSE AQUI >>>>> {original_file_name}')
        #     print(f'original_file_name = {original_file_name}')
        #     print((f'pictures/{y}/{m}/{original_file_name}'))
        #     media_root_path = settings.MEDIA_ROOT
        #     # Salvar o novo arquivo com o nome customizado
        #     if default_storage.exists(f'contact/media/pictures/{y}/{m}/{original_file_name}'):
        #         print(f'entrei no >>>>> if default_storage.exists')
        #         file_content = default_storage.open(original_file_name).read()
        #         default_storage.save(f'{new_file_name}', ContentFile(file_content))
                

        #         # Atualizar o campo 'picture' no modelo Contact
        #         obj.picture.name = new_file_name
        #         default_storage.save()
        #         default_storage.delete(original_file_name)

        # super().save_model(request, obj, form, change)



@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name',
    ordering = '-id', #Sinal negativa para listar em ordem decrescente
