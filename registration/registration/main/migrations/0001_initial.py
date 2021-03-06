# Generated by Django 3.2.12 on 2022-03-16 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VehicleBrand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(choices=[('VW', 'VW'), ('Mercedes', 'Mercedes'), ('Opel', 'Opel'), ('Audi', 'Audi'), ('BMW', 'BMW'), ('Peugeot', 'Peugeot'), ('Ford', 'Ford'), ('Toyota', 'Toyota'), ('Renault', 'Renault'), ('Citroen', 'Citroen'), ('Alfa Romeo', 'Alfa Romeo'), ('Fiat', 'Fiat')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='VehicleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(choices=[('Passat', 'Passat'), ('E Class', 'E Class'), ('S Class', 'S Class'), ('C Class', 'C Class'), ('G Class', 'G Class'), ('E 90', 'E 90'), ('E 60', 'E 60'), ('F 10', 'F 10'), ('Mustang', 'Mustang')], max_length=7)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.vehiclebrand')),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.DateField()),
                ('price', models.FloatField()),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.vehiclebrand')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.vehiclemodel')),
            ],
        ),
    ]
