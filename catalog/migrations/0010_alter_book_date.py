# Generated by Django 3.2.6 on 2022-06-08 10:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_auto_20220608_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 8, 10, 53, 49, 832533, tzinfo=utc)),
        ),
    ]
