from django.shortcuts import render, redirect

from Expenses_tracker.core.calculations import calculate_budget
from Expenses_tracker.profiles.forms import ProfileForm
from Expenses_tracker.profiles.models import Profile


def get_profile():
    context = {
        'profile': Profile.objects.first(),
        'result': calculate_budget(),
    }
    return context


def profile_page(request):
    return render(request, 'profile.html', get_profile())


def edit_profile(request):
    if request.method == 'GET':
        return render(request, 'profile-edit.html', get_profile())
    form = ProfileForm(request.POST, instance=get_profile()['profile'])
    if form.is_valid():
        form.save()
        return redirect('profile page')
    return render(request, 'profile-edit.html', get_profile())


def delete_profile(request):
    if request.method == 'GET':
        return render(request, 'profile-delete.html', get_profile())
    profile = get_profile()
    profile['profile'].delete()
    return redirect('home page')