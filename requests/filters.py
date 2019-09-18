import django_filters
from trips import models

class TripFilter(django_filters.FilterSet):
    class Meta:
        model = models.Trip
        fields = ['destination']
