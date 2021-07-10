from django import forms

from djangoProject.pet.models import Pet


class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        type = forms.ChoiceField(
            required=True,
            widget=forms.Select(
                attrs={
                    'class': 'form-control'
                }
            )
        )
        name = forms.CharField(
            required=True,
            widget=forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            )
        )
        age = forms.IntegerField(
            required=True,
            widget=forms.TextInput(
             attrs={
                 'class': 'form-control',
                 'type': 'number'
             }
            )
        )
        image_url = forms.FileField(required=True, widget=forms.FileInput(
            attrs={
                'class': 'form-control'
            }))
        description = forms.CharField(required=True, widget=forms.Textarea(attrs={
            'class': 'form-control rounded-2'
        }))

        fields = '__all__'
