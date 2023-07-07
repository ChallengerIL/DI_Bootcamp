from django.db import models


class Movie(models.Model):

    movie_id = models.IntegerField()
    title = models.CharField(max_length=100)
    favorite = models.BooleanField(default=False)
    watched = models.BooleanField(default=False)
    watchlist = models.BooleanField(default=False)

    def __str__(self):
        return self.title
