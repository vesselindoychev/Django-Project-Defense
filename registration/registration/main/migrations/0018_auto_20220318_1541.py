# Generated by Django 3.2.12 on 2022-03-18 13:41

from django.db import migrations, models
import registration.common.validators


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_advert'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vehicle',
            options={},
        ),
        migrations.AddField(
            model_name='vehicle',
            name='fuel_type',
            field=models.CharField(choices=[('Diesel', 'Diesel'), ('Gasoline', 'Gasoline'), ('Electric', 'Electric')], default=1, max_length=8),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='engine',
            field=models.CharField(max_length=10, validators=[registration.common.validators.validate_car_model]),
        ),
    ]