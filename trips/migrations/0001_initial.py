# Generated by Django 2.2.1 on 2019-08-14 10:00

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('date_request', models.DateTimeField(default=datetime.datetime(2019, 8, 14, 5, 0, 43, 688233))),
                ('origin', models.CharField(max_length=100)),
                ('places', models.SmallIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('destination', models.CharField(choices=[('BLVD', 'Boulevard ASIA'), ('PH', 'Punta Hermosa'), ('PARACAS', 'Paracas'), ('ELROS', 'El Rosario'), ('CERROA', 'Cerro Azul')], max_length=64)),
                ('description', models.TextField(blank=True, default='')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trips', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
