# Generated by Django 3.2.12 on 2022-03-16 13:53

import django.core.validators
from django.db import migrations, models
import registration.common.validators


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20220315_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(2), registration.common.validators.validate_only_letters]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(2), registration.common.validators.validate_only_letters]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(upload_to='profiles/', validators=[registration.common.validators.MaxImageSizeInMbValidator(5)]),
        ),
    ]
