# Generated by Django 3.2.12 on 2022-03-16 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20220316_1626'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehiclemodel',
            name='brand',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.vehiclebrand'),
            preserve_default=False,
        ),
    ]