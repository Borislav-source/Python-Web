from django import forms

from Expenses_tracker.profiles.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
