# Generated by Django 3.2.12 on 2022-03-16 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vehiclebrand',
            options={'ordering': ['brand']},
        ),
        migrations.AlterModelOptions(
            name='vehiclemodel',
            options={'ordering': ['brand', 'model']},
        ),
        migrations.AlterUniqueTogether(
            name='vehiclebrand',
            unique_together={('brand',)},
        ),
        migrations.AlterUniqueTogether(
            name='vehiclemodel',
            unique_together={('brand', 'model')},
        ),
    ]
