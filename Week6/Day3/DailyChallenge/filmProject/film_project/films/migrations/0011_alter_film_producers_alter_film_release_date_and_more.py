# Generated by Django 4.2.1 on 2023-06-07 09:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0010_alter_film_release_date_alter_review_review_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='producers',
            field=models.ManyToManyField(related_name='films', to='films.producer'),
        ),
        migrations.AlterField(
            model_name='film',
            name='release_date',
            field=models.DateField(default=datetime.datetime(2023, 6, 7, 9, 49, 53, 232508, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='review',
            name='review_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 7, 9, 49, 53, 233846, tzinfo=datetime.timezone.utc)),
        ),
    ]
