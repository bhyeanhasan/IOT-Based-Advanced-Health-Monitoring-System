# Generated by Django 5.0.6 on 2024-06-27 10:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_temperature', '0004_alter_temperature_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sensors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_temp', models.FloatField(blank=True, null=True)),
                ('ecg', models.FloatField(blank=True, null=True)),
                ('time', models.DateTimeField(default=datetime.datetime(2024, 6, 27, 16, 33, 26, 620166))),
            ],
        ),
        migrations.DeleteModel(
            name='Temperature',
        ),
    ]
