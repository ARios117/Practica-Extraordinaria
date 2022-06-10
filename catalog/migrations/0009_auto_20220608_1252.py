# Generated by Django 3.2.6 on 2022-06-08 10:52

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_auto_20220608_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 8, 10, 52, 15, 915077, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='vote',
            name='book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='votes', to='catalog.book'),
        ),
    ]