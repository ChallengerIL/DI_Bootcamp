# Generated by Django 4.2.1 on 2023-06-05 07:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0007_alter_film_release_date_alter_review_review_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='release_date',
            field=models.DateField(default=datetime.datetime(2023, 6, 5, 7, 23, 27, 868309, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='review',
            name='review_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 5, 7, 23, 27, 869465, tzinfo=datetime.timezone.utc)),
        ),
    ]
