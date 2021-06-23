from django import forms


class UserFormModel(forms.Form):
    name = forms.CharField()
    age = forms.IntegerField(
        widget=forms.NumberInput
    )
    Email = forms.EmailField(
        widget=forms.EmailInput
    )
    Password = forms.CharField(
        widget= forms.PasswordInput
    )
    Text = forms.CharField(
        widget=forms.Textarea
    )


class TodoForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField(
        widget=forms.Textarea()
    )
