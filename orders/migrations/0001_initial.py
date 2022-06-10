# Generated by Django 3.2.6 on 2021-11-22 16:49

import catalog.validators
import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('postal_code', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=100)),
                ('created', models.DateTimeField(default=datetime.datetime(2021, 11, 22, 16, 49, 23, 273814, tzinfo=utc))),
                ('updated', models.DateTimeField(default=datetime.datetime(2021, 11, 22, 16, 49, 23, 273839, tzinfo=utc))),
                ('paid', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, default=0, editable=False, max_digits=10)),
                ('quantity', models.IntegerField(default=1, validators=[catalog.validators.validar_gt_0])),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.book')),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='orders.order')),
            ],
        ),
    ]