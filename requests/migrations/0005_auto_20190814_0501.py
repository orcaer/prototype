# Generated by Django 2.2.1 on 2019-08-14 10:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requests', '0004_auto_20190814_0500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requests',
            name='date_request',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 14, 5, 1, 1, 197609)),
        ),
    ]
