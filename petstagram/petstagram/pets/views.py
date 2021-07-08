from django.shortcuts import render, redirect

from common.forms import CommentForm
from petstagram.common.models import Comment
from pets.forms import CreatePetForm
from petstagram.pets.models import Pet, Like
from django_cleanup.signals import cleanup_pre_delete


def pet_all(request):
    context = {
        'Pets': Pet.objects.all()
    }
    return render(request, 'pet_list.html', context)


def pet_detail(request, pk):
    if request.method == 'GET':
        pet_comments = []
        comments = Comment.objects.all()
        for comment in comments:
            if comment.pet_id == pk:
                pet_comments.append(comment)
        context = {
            'pet': Pet.objects.get(pk=pk),
            'comments': pet_comments,
            'comment_form': CommentForm(),
        }

        return render(request, 'pet_detail.html', context)
    form = CommentForm(request.POST)
    if form.is_valid():
        text = form.cleaned_data['comment']
        form = Comment(text=text, pet_id=pk)
        form.save()
        pet_comments = []
        comments = Comment.objects.all()
        for comment in comments:
            if comment.pet_id == pk:
                pet_comments.append(comment)
        context = {
            'pet': Pet.objects.get(pk=pk),
            'comments': pet_comments,
            'comment_form': CommentForm(),
        }

        return render(request, 'pet_detail.html', context)


def like(request, pk):
    pet = Pet.objects.get(pk=pk)
    new_like = Like(
        pet=pet,
    )
    new_like.save()
    context = {
        'likes': Like.objects.all()
    }
    return redirect('pet details', pet.id)


def create(request):
    if request.method == 'GET':
        context = {
            'form': CreatePetForm(),
        }
        return render(request, 'pet_create.html', context)

    form = CreatePetForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('all pets list')

    context = {
        'form': form,
    }
    return render(request, 'pet_create.html', context)


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