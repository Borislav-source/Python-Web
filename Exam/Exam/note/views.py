from django.shortcuts import render, redirect

from Exam.note.forms import NoteForm, DeleteNoteForm
from Exam.note.models import Note
from Exam.people.models import Profile


def home_page(request):
    profile = Profile.objects.first()
    if not profile:
        return redirect('profile create')
    else:
        context = {
            'profile': profile,
            'notes': Note.objects.all(),
        }
        return render(request, 'home-with-profile.html', context)


def add_note(request):
    if request.method == 'GET':
        context = {
            'form': NoteForm(),
        }
        return render(request, 'note-create.html', context)
    form = NoteForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('home page')
    context = {
        'form': form
    }
    return render(request, 'note-create.html', context)


def edit_note(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'form': NoteForm(instance=note),
        }
        return render(request, 'note-edit.html', context)
    form = NoteForm(request.POST, instance=note)
    if form.is_valid():
        form.save()
        return redirect('home page')
    context = {
        'form': form,
    }
    return render(request, 'note-edit.html', context)


def note_info(request, pk):
    note = Note.objects.get(pk=pk)
    context = {
        'note': note
    }
    return render(request, 'note-details.html', context)


def delete_note(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'form': DeleteNoteForm(instance=note)
        }
        return render(request, 'note-delete.html', context)

    note.delete()
    return redirect('home page')
