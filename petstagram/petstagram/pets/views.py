from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from common.forms import CommentForm
from pets.decorators import allowed_users
from petstagram.common.models import Comment
from pets.forms import CreatePetForm
from petstagram.pets.models import Pet, Like
from django_cleanup.signals import cleanup_pre_delete


def pet_all(request):
    context = {
        'Pets': Pet.objects.all()
    }
    return render(request, 'pet_list.html', context)


@login_required
def pet_detail(request, pk):
    pet = Pet.objects.get(pk=pk)
    context = {
        'pet': pet,
        'is_owner': pet.user == request.user,
        'like_object': pet.like_set.filter(user_id=request.user.id),
        'comments': pet.comment_set.all(),
        'comment_form': CommentForm()
    }
    return render(request, 'pet_detail.html', context)


def comment_pet(request, pk):
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.pet = Pet.objects.get(pk=pk)
        comment.user = request.user
        comment.save()
    return redirect('pet details', pk)


def like(request, pk):
    pet = Pet.objects.get(pk=pk)
    like_object = pet.like_set.filter(user_id=request.user.id).first()
    if not like_object:
        new_like = Like(
            pet=pet,
            user=request.user,
        )
        new_like.save()
    else:
        like_object.delete()
    return redirect('pet details', pet.id)


@login_required
@allowed_users(['Management'])
def create(request):
    if request.method == 'GET':
        context = {
            'form': CreatePetForm(),
        }
        return render(request, 'pet_create.html', context)

    form = CreatePetForm(request.POST, request.FILES)
    if form.is_valid():
        pet = form.save(commit=False)
        pet.user = request.user
        pet.save()
        return redirect('all pets list')

    context = {
        'form': form,
    }
    return render(request, 'pet_create.html', context)


@allowed_users(['Management'])
def edit(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'edit_form': CreatePetForm(instance=pet)
        }
        return render(request, 'pet_edit.html', context)
    form = CreatePetForm(request.POST, request.FILES, instance=pet)
    if form.is_valid():
        form.save()
        return redirect('pet details', pet.id)
    context = {
        'edit_form': form
    }
    return render(request, 'pet_edit.html', context)


@allowed_users(['Management'])
def delete(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'pet': pet
        }
        return render(request, 'pet_delete.html', context)

    elif request.method == 'POST':
        pet.delete()
        context = {
            'Pets': Pet.objects.all()
        }
        return render(request, 'pet_list.html', context)
