# Generated by Django 3.2.12 on 2022-03-16 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20220316_1742'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carmodel',
            name='make',
        ),
        migrations.DeleteModel(
            name='Car',
        ),
        migrations.DeleteModel(
            name='CarMake',
        ),
        migrations.DeleteModel(
            name='CarModel',
        ),
    ]
