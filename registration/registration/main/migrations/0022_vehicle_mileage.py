# Generated by Django 3.2.12 on 2022-03-18 14:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_vehicle_euro_standard'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='mileage',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(0)]),
            preserve_default=False,
        ),
    ]
