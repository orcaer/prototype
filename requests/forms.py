from django import forms

from . import models

class RequestsForm(forms.ModelForm):
    class Meta:
        model = models.Requests
        fields = ['destination', 'address', 'date_request']
        widgets = {
            'date': forms.DateTimeInput()
        }
