from django import forms


def name_validate(value):
    if not value[0] == value[0].upper():
        raise forms.ValidationError('Name needs to start with uppercase letter')


def age_validator(value):
    if not value >= 0:
        raise forms.ValidationError("Age cannot be less than zero")


def password_validator(value):
    if not value.isalnum():
        raise forms.ValidationError('Enter a valid password')


class UserFormModel(forms.Form):
    name = forms.CharField(
        min_length=6,
        validators=[
            name_validate,
        ]
    )
    age = forms.IntegerField(
        widget=forms.NumberInput,
        validators=[
            age_validator,
        ]
    )
    Email = forms.EmailField(
        widget=forms.EmailInput
    )
    Password = forms.CharField(
        min_length=8,
        widget=forms.PasswordInput,
        validators=[
            password_validator,
        ]
    )
    Text = forms.CharField(
        widget=forms.Textarea
    )


class TodoForm(forms.Form):
    title = forms.CharField(
        label='title',
        max_length=20,
    )
    description = forms.CharField(
        widget=forms.Textarea()
    )
