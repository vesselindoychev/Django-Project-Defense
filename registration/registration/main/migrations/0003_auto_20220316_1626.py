# Generated by Django 3.2.12 on 2022-03-16 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20220316_1615'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vehiclebrand',
            options={},
        ),
        migrations.AlterModelOptions(
            name='vehiclemodel',
            options={},
        ),
        migrations.AlterUniqueTogether(
            name='vehiclebrand',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='vehiclemodel',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='vehiclemodel',
            name='brand',
        ),
    ]
