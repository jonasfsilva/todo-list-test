# Generated by Django 2.1.7 on 2021-05-04 19:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20210504_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created_at',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 5, 4, 16, 21, 4, 12222)),
        ),
    ]
