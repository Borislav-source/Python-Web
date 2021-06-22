from django.shortcuts import render, redirect

from Forms_exercise.forms import UserFormModel


def index(request):
    if request.method == 'POST':
        form = UserFormModel(request.POST)
        if form.is_valid():
            fields = ['name', 'age', 'Email', 'Password', 'Text']
            print('VALIDATION SUCCESS')
            [print(f'{field.upper()}: {form.cleaned_data[field]}') for field in fields]
            return redirect('/forms/')
        else:
            print(form.errors)
    else:
        context = {
            'form': UserFormModel()
        }
        return render(request, 'todo_app/create.html', context)


# def print_results(request):
#     if request.method == 'POST':
#         form = UserFormModel(request.POST)
#         if form.is_valid():
#             fields = ['name', 'age', 'Email', 'Password', 'Text']
#             [print(form.cleaned_data[field]) for field in fields]
#             return redirect('/forms/')