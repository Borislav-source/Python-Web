from django import forms

from Exam.people.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'image_url': 'Link to Profile Image'

        }
        fields = '__all__'

