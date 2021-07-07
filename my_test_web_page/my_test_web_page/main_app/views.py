from django.shortcuts import render, redirect

from my_test_web_page.main_app.form import ProfileForm
from my_test_web_page.main_app.models import Profile


def index(request):
    if request.method == 'GET':
        context = {
            'form': ProfileForm(),
            'profiles': Profile.objects.all()
        }
        return render(request, 'main_app/index.html', context)
    else:
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save()
            profile.save()
            return redirect('root page')
        return render(request, 'main_app/index.html', {'form': form, 'profiles': Profile.objects.all()})
