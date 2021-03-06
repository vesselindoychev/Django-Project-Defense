# Generated by Django 3.2.12 on 2022-03-15 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='picture',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
