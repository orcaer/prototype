# Generated by Django 2.2.1 on 2019-08-18 11:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0002_auto_20190814_0501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='date_request',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 18, 6, 17, 7, 32776)),
        ),
    ]
