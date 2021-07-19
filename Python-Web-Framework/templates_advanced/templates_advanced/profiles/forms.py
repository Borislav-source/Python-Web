from django import forms

from templates_advanced.profiles.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('is_done', 'user',)
