from django.shortcuts import render, redirect
from Exam.note.models import Note
from Exam.people.forms import ProfileForm
from Exam.people.models import Profile


def create_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')
        else:
            context = {
                'form': form
            }
            return render(request, 'home-no-profile.html', context)
    context = {
        'form': ProfileForm()
    }
    return render(request, 'home-no-profile.html', context)


def profile_info(request):
    profile = Profile.objects.first()
    context = {
        'profile': profile,
        'notes_count': Note.objects.all().count(),
    }
    return render(request, 'profile.html', context)


def delete_profile(request):
    profile = Profile.objects.first()
    notes = Note.objects.all()
    notes.delete()
    profile.delete()
    return redirect('home page')
