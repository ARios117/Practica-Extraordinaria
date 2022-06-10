# Generated by Django 3.2.6 on 2022-06-08 10:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20211220_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 8, 10, 40, 53, 971198, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 8, 10, 40, 53, 971224, tzinfo=utc)),
        ),
    ]
