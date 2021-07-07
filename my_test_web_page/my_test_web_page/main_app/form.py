from django import forms

from my_test_web_page.main_app.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'custom-file-input'}),
        }
        fields = '__all__'
