# Generated by Django 4.2.1 on 2023-06-07 09:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0012_alter_film_producers_alter_film_release_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='release_date',
            field=models.DateField(default=datetime.datetime(2023, 6, 7, 9, 54, 11, 119178, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='review',
            name='review_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 7, 9, 54, 11, 120555, tzinfo=datetime.timezone.utc)),
        ),
    ]
