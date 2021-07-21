from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from petstagram.pets.models import Pet
from petstagram.accounts.forms import ProfileForm, SignupForm, SigninForm
from petstagram.accounts.models import UserProfile


def user_profile(request, pk):
    user = UserProfile.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile details', pk)
        return render(request, 'accounts/user_profile.html', {'form': form})
    context = {
        'form': ProfileForm(instance=user),
        'pets': Pet.objects.filter(user_id=pk),
        'profile': user,
    }

    return render(request, 'accounts/user_profile.html', context)


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sign in user')
        return render(request, 'accounts/signup.html', {'form': form})

    else:
        context = {
            'form': SignupForm(),
        }

        return render(request, 'accounts/signup.html', context)


def signin(request):
    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home page')
        return render(request, 'registration/sign-in.html', {'form': form})
    else:
        context = {
            'form': SigninForm(),
        }

        return render(request, 'registration/sign-in.html', context)


def signout(request):
    logout(request)
    return redirect('home page')
