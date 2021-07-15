from django import forms


class SignForm(forms.Form):
    username = forms.CharField(
        max_length=15,
    )
    password = forms.CharField(
        max_length=15,
        widget=(
            forms.PasswordInput()
        )
    )
