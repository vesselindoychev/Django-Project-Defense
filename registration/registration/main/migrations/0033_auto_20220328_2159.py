# Generated by Django 3.2.12 on 2022-03-28 18:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0032_contact_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='user',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='user',
        ),
    ]
