# Generated by Django 4.2.3 on 2023-07-05 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_id', models.IntegerField()),
                ('title', models.CharField(max_length=100)),
                ('release_year', models.IntegerField()),
                ('release_date', models.DateField()),
                ('poster_url', models.URLField()),
                ('budget', models.IntegerField()),
                ('genres', models.CharField(max_length=1000)),
                ('imdb_id', models.CharField(max_length=100)),
                ('language', models.CharField(max_length=50)),
                ('plot', models.CharField(max_length=1000)),
                ('popularity', models.DecimalField(decimal_places=3, max_digits=10)),
            ],
        ),
    ]
