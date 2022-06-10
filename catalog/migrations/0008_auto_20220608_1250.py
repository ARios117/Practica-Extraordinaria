# Generated by Django 3.2.6 on 2022-06-08 10:50

import catalog.validators
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog', '0007_alter_book_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 8, 10, 50, 2, 50543, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='book',
            name='score',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4, validators=[catalog.validators.validar_gt_0, catalog.validators.validar_lt_10]),
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(default=0, validators=[catalog.validators.validar_gt_0, catalog.validators.validar_lt_10])),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.book')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['book', 'user', 'score'],
            },
        ),
    ]
