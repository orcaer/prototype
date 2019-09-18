from django.db import models
from django.urls import reverse
from datetime import datetime
# Create your models here.
from django.contrib.auth import get_user_model
User = get_user_model()

class Requests(models.Model):
    DESTINATIONS = [
    ('BLVD', 'Boulevard ASIA'),
    ('PH', 'Punta Hermosa'),
    ('PARACAS', 'Paracas'),
    ('ELROS', 'El Rosario'),
    ('CERROA',  'Cerro Azul')
    ]
    user = models.ForeignKey(User, related_name="requests", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now=True, null=False)
    date_request = models.DateTimeField(auto_now = False, default = datetime.now(), null = False, editable = True)
    destination = models.CharField(max_length=64, choices = DESTINATIONS)
    address = models.TextField(blank = True, default = '')

    def __str__(self):
        return self.address

    def get_absolute_url(self):
        return reverse('home')
