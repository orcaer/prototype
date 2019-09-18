from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from datetime import datetime
User = get_user_model()

class Trip(models.Model):
    DESTINATIONS = [
    ('BLVD', 'Boulevard ASIA'),
    ('PH', 'Punta Hermosa'),
    ('PARACAS', 'Paracas'),
    ('ELROS', 'El Rosario'),
    ('CERROA',  'Cerro Azul')
    ]
    SPACES = [
    (1,1), (2,2), (3,3), (4,4), (5,5)
    ]
    user = models.ForeignKey(User, related_name="trips", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now=True, null=False)
    date_request = models.DateTimeField(auto_now = False, default = datetime.now(), null = False, editable = True)
    origin = models.CharField(max_length=100, null=False)
    places = models.SmallIntegerField(choices = SPACES, null=False)
    destination = models.CharField(max_length=64, choices = DESTINATIONS)
    description = models.TextField(blank = True, default = '')

    def __str__(self):
        return self.destination

    def get_absolute_url(self):
        return reverse('trips:confirm_trip', kwargs={
                                    'username': self.user.username,
                                    'pk': self.pk}
                                    )

# Create your models here.
