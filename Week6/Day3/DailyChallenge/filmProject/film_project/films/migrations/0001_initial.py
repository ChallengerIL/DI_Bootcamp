# Generated by Django 4.2.1 on 2023-06-07 07:56

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('release_date', models.DateField(default=datetime.datetime(2023, 6, 7, 7, 56, 56, 201890, tzinfo=datetime.timezone.utc))),
                ('available_in_countries', models.ManyToManyField(related_name='films', to='films.country')),
                ('category', models.ManyToManyField(related_name='films', to='films.category')),
                ('created_in_country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='country_of_origin', to='films.country')),
                ('director', models.ManyToManyField(related_name='films', to='films.director')),
            ],
        ),
        migrations.CreateModel(
            name='Producer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_text', models.TextField()),
                ('rating', models.IntegerField()),
                ('review_date', models.DateTimeField(default=datetime.datetime(2023, 6, 7, 7, 56, 56, 203327, tzinfo=datetime.timezone.utc))),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='films.film')),
            ],
        ),
        migrations.AddField(
            model_name='film',
            name='producers',
            field=models.ManyToManyField(db_constraint=False, related_name='films', to='films.producer'),
        ),
    ]