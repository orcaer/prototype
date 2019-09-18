from django import forms

from . import models

class TripForm(forms.ModelForm):
    class Meta:
        model = models.Trip
        fields = ['origin', 'destination', 'places','description','date_request']
