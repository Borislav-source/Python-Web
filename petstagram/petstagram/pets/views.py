from django.shortcuts import render, redirect

from petstagram.pets.models import Pet, Like


def pet_all(request):
    context = {
        'Pets': Pet.objects.all()
    }
    return render(request, 'pet_list.html', context)


def pet_detail(request, pk):
    context = {
        'pet': Pet.objects.get(pk=pk)
    }

    return render(request, 'pet_detail.html', context)


def like(request, pk):
    pet = Pet.objects.get(pk=pk)
    new_like = Like(
        pet=pet,
    )
    new_like.save()
    context ={
        'likes': Like.objects.all()
    }
    return redirect('pet details', pet.id)