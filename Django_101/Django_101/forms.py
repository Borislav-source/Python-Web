from django import forms
from .models import Person


class MemberForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = [
            'fname',
            'lname',
            'email',
            'password',
            'age',
        ]