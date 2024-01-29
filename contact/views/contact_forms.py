from django.shortcuts import render , redirect, get_object_or_404
from contact.forms import Contact_Form
from django.urls import reverse
from contact.models import Contact
from contact.forms import ConfirmationForm
from django.contrib.auth.decorators import login_required
import os
from datetime import datetime
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

@login_required(login_url='contact:login')
def create(request):
    
    form_action = reverse('contact:create')
    

    if request.method == 'POST':
        form = Contact_Form(request.POST, request.FILES)
        
        context = {
            'form' : form,
            'form_action': form_action,
        }

        
        if form.is_valid():
            contact = form.save(commit=False)
            contact.owner = request.user
            contact.save()
            # contact = form.save(commit=False)
            # contact.show = False
            # contact.save()
            # if contact.picture:
            #     original_file_name = contact.picture.name

            #     # Criar novo nome de arquivo
            #     date_str = datetime.now().strftime("%Y%m%d")
            #     y = datetime.now().strftime("%Y")
            #     m = datetime.now().strftime("%m")
            #     d = datetime.now().strftime("%d")
            #     file_name = os.path.basename(original_file_name)
            #     new_file_name = f'pictures/{y}/{m}/{d}_{contact.id}_{file_name}'

            #     # Copiar o arquivo para o novo nome
            #     if default_storage.exists(original_file_name):
            #         file_content = default_storage.open(original_file_name).read()
            #         default_storage.save(new_file_name, ContentFile(file_content))

            #         # Atualizar o campo 'picture' no modelo Contact
            #         contact.picture.name = new_file_name
            #         contact.save()

            #         # Excluir o arquivo antigo
            #         default_storage.delete(original_file_name)
            #         print(f'É ESSE AQUI >>>>> {original_file_name}')

                
            
            return redirect('contact:update', contact_id= contact.id)

        return render(
        request,
        'contact/create.html',
        context
        )

    context = {
        'form' : Contact_Form(),
        'form_action': form_action,
    }

    return render(
        request,
        'contact/create.html',
        context
        )

@login_required(login_url='contact:login')
def update(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id, show=True , owner = request.user)
    form_action = reverse('contact:update', args=(contact_id,))

    if request.method == 'POST':
        form = Contact_Form(request.POST, request.FILES, instance=contact)
        old_name = contact.picture.name
        
        context = {
            'form' : form,
            'form_action': form_action,
        }

        if form.is_valid():
            
            # contact = form.save(commit=False)
            # contact.show = False
            contact.save()
            # if 'picture' in request.FILES:
                
            #     new_picture = request.FILES['picture']
            #     print(new_picture.name)
            #     print(contact.picture.name)
            #     if new_picture.name != old_name:
            #         print('ENTROU')
            #         original_file_name = new_picture.name
            #         date_str = datetime.now().strftime("%Y%m%d")
            #         y = datetime.now().strftime("%Y")
            #         m = datetime.now().strftime("%m")
            #         d = datetime.now().strftime("%d")
            #         file_name = os.path.basename(original_file_name)
            #         new_file_name = f'{d}_{contact.id}_{file_name}'
            #         # contact.picture.name = new_file_name
            #         print(f'ESSE AQUI >>> {new_file_name}')
            #         contact.picture.save(new_file_name, ContentFile(new_picture.read()), save=False)
                

            # contact = form.save()


            return redirect('contact:update', contact_id= contact.id)

        return render(
        request,
        'contact/create.html',
        context
        )

    context = {
        'form' : Contact_Form(instance=contact),
        'form_action': form_action,
    }

    return render(
    request,
    'contact/create.html',
    context
    )

@login_required(login_url='contact:login')
def delete(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id, show=True, owner = request.user)

    # Se a requisição for POST, crie o ConfirmationForm com dados do POST
    if request.method == 'POST':
        confirmation_form = ConfirmationForm(request.POST)

        # Verifica se o formulário de confirmação é válido
        if confirmation_form.is_valid():
            contact.delete()
            return redirect('contact:index')
    else:
        # Se a requisição não for POST, crie um ConfirmationForm vazio
        confirmation_form = ConfirmationForm()

    context = {
        'form': Contact_Form(instance=contact),  # Formulário de edição do contato
        'confirmation_form': confirmation_form,  # Formulário de confirmação
        'contact': contact  # Informações do contato
    }

    return render(
        request,
        'contact/update.html',  # O template de edição do contato
        context
    )
