from django.db import models


class Gif(models.Model):

    title = models.CharField(max_length=100)
    url = models.URLField()
    uploader_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Category(models.Model):

    name = models.CharField(max_length=100)
    gifs = models.ManyToManyField(Gif, related_name='gifs', blank=True)

    def __str__(self):
        return self.name