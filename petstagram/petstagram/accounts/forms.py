from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from petstagram.accounts.models import UserProfile

UserModel = get_user_model()


class ProfileForm(forms.ModelForm):
    class Meta:
        mode = UserProfile
        fields = ('profile_picture',)


class SignupForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('email',)


class SigninForm(forms.Form):
    user = None

    email = forms.EmailField()
    password = forms.CharField(
        widget=forms.PasswordInput(),
    )

    def clean_password(self):
        self.user = authenticate(
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password']
        )
        if not self.user:
            raise ValidationError('Email and/or password are incorrect')

    def save(self):
        return self.user
