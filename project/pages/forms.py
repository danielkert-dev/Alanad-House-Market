from django import forms
from .models import FormHouse

class FormHouseForm(forms.ModelForm):
    class Meta:
        model = FormHouse
        exclude = [id]  # List any fields you want to exclude from the form

        widgets = {
            'date_added': forms.DateInput(attrs={'type': 'date'}),
        }