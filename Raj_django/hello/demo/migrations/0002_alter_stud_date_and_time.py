# Generated by Django 5.1.3 on 2024-12-11 10:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stud',
            name='date_and_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 12, 11, 15, 37, 3, 650117)),
        ),
    ]
