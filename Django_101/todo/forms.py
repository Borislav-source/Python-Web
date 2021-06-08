from django import forms


class TodoForm(forms.Form):

    title = forms.CharField(
        widget=forms.TextInput
    )

    description = forms.CharField(
        widget=forms.Textarea,
    )