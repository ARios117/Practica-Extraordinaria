# Generated by Django 3.2.6 on 2022-06-09 08:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0018_auto_20220608_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 9, 8, 45, 30, 710258, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 9, 8, 45, 30, 710283, tzinfo=utc)),
        ),
    ]