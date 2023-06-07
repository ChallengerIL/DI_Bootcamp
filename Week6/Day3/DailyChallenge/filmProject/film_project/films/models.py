from django.db import models
from django.utils import timezone


class Country(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Category(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Director(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Producer(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Film(models.Model):

    title = models.CharField(max_length=100)
    release_date = models.DateField(default=timezone.now())
    created_in_country = models.ForeignKey(Country, related_name='country_of_origin', on_delete=models.CASCADE)
    available_in_countries = models.ManyToManyField(Country, related_name='films')
    category = models.ManyToManyField(Category, related_name='films')
    director = models.ManyToManyField(Director, related_name='films')
    producers = models.ManyToManyField(Producer, related_name='films', blank=True)

    def __str__(self):
        return self.title


class Review(models.Model):

    film = models.ForeignKey(Film, related_name='reviews', on_delete=models.CASCADE)
    review_text = models.TextField()
    rating = models.IntegerField()
    review_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return f"{self.film}: {self.review_text[:30]}"
