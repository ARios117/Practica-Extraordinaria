# Generated by Django 3.2.6 on 2021-12-20 15:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20211220_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 20, 15, 1, 47, 230504, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 20, 15, 1, 47, 230544, tzinfo=utc)),
        ),
    ]
