from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

UserModel = get_user_model()


class SignForm(forms.Form):
    user = None

    email = forms.EmailField(
    )
    password = forms.CharField(
        widget=(
            forms.PasswordInput()
        ))

    def clean_password(self):
        self.user = authenticate(
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password'], )
        if not self.user:
            raise ValidationError('Email and/or Password is incorrect!')

    def save(self):
        return self.user


class SignUpForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('email',)
