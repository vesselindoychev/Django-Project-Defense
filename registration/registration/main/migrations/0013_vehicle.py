# Generated by Django 3.2.12 on 2022-03-16 15:56

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import registration.common.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0012_auto_20220316_1746'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(choices=[('VW', 'VW'), ('Mercedes', 'Mercedes'), ('Opel', 'Opel'), ('Audi', 'Audi'), ('BMW', 'BMW'), ('Peugeot', 'Peugeot'), ('Ford', 'Ford'), ('Toyota', 'Toyota'), ('Renault', 'Renault'), ('Citroen', 'Citroen'), ('Alfa Romeo', 'Alfa Romeo'), ('Fiat', 'Fiat')], max_length=10)),
                ('model', models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(3), registration.common.validators.validate_car_model])),
                ('price', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
                ('engine', models.CharField(choices=[('Diesel', 'Diesel'), ('Gasoline', 'Gasoline'), ('Electric', 'Electric')], max_length=8)),
                ('gearbox', models.CharField(choices=[('Manual Transmission', 'Manual Transmission'), ('Automatic Transmission', 'Automatic Transmission')], max_length=22)),
                ('manufacture_date', models.IntegerField()),
                ('power', models.IntegerField()),
                ('type', models.CharField(choices=[('Sedan', 'Sedan'), ('Coupe', 'Coupe'), ('Station Wagon', 'Station Wagon'), ('Hatchback', 'Hatchback'), ('SUV', 'SUV'), ('Minivan', 'Minivan'), ('Pickup Truck', 'Pickup Truck'), ('Van', 'Van'), ('Convertible', 'Convertible')], max_length=13)),
                ('location', models.CharField(choices=[('Plovdiv', 'Plovdiv'), ('Sofia', 'Sofia'), ('Burgas', 'Burgas'), ('Varna', 'Varna'), ('Veliko Turnovo', 'Veliko Turnovo'), ('Pazardzhik', 'Pazardzhik'), ('Yambol', 'Yambol'), ('Blagoevgrad', 'Blagoevgrad'), ('Pernik', 'Pernik'), ('Stara Zagora', 'Stara Zagora'), ('Karlovo', 'Karlovo'), ('Haskovo', 'Haskovo'), ('Sliven', 'Sliven'), ('Ruse', 'Ruse')], max_length=14)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('id',),
            },
        ),
    ]
