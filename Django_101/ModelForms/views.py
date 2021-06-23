from django.shortcuts import render, redirect

from ModelForms.forms import BookForm
from ModelForms.models import Book


def index(request):
    context = {
        'books': Book.objects.all()
    }
    return render(request, 'ModelForm_templates/index.html', context)


def create(request):
    form = BookForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('all books')
    print(form.errors)
    context = {
        'form': form
    }
    return render(request, 'ModelForm_templates/create.html', context)


def edit(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'GET':
        form = BookForm(instance=book)
        context = {
            'form': form
        }
        return render(request, 'ModelForm_templates/edit.html', context)
    else:
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('all books')
        context = {
            'form': form
        }
        return render(request, 'ModelForm_templates/edit.html', context)