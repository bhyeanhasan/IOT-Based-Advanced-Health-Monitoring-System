# Generated by Django 5.0.6 on 2024-07-10 06:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_temperature', '0006_sensors_gsr_sensors_hr_alter_sensors_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensors',
            name='ir',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='sensors',
            name='red',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='sensors',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 10, 12, 34, 25, 477172)),
        ),
    ]
