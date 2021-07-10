from django.shortcuts import render, redirect

from djangoProject.common.forms import CommentForm
from djangoProject.common.models import Comment
from djangoProject.pet.forms import PetForm
from djangoProject.pet.models import Pet, Like


def index(request):
    return render(request, 'landing_page.html')


def pet_all(request):
    context = {
        'Pets': Pet.objects.all()
    }
    return render(request, 'pet_list.html', context)


def create_pet(request):
    if request.method == 'GET':
        context = {
            'form': PetForm()
        }
        return render(request, 'pet_create.html', context)
    form = PetForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('pet_all')
    return render(request, 'pet_create.html', {'form': form})


def pet_details(request, pk):
    pet = Pet.objects.get(pk=pk)
    comments = Comment.objects.all()
    pet_comments = [com for com in comments if pet.id == com.pet.id ]

    context = {
        'pet': pet,
        'comments': pet_comments,
        'comment_form': CommentForm()
    }
    return render(request, 'pet_detail.html', context)


def like(request, pk):
    pet = Pet.objects.get(pk=pk)
    new_like = Like(pet=pet)
    new_like.save()
    return redirect('details', pet.id)


def edit_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'form': PetForm(instance=pet)
        }
        return render(request, 'pet_edit.html', context)
    form = PetForm(request.POST, request.FILES, instance=pet)
    if form.is_valid():
        form.save()
        return redirect('details', pet.id)
    return render(request, 'pet_edit.html', {'form': form})


def delete(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == 'GET':
        return render(request, 'pet_delete.html', {'pet': pet})
    pet.delete()
    return redirect('pet_all')


def comment(request, pk):
    pet = Pet.objects.get(pk=pk)
    form = CommentForm(request.POST)
    text = request.POST['comment']
    new_comment = Comment(pet=pet, comment=text)
    new_comment.save()
    return redirect('details', pet.id)