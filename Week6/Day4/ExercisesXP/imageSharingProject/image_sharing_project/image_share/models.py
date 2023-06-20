from django.db import models
from django.contrib.auth.models import User


class Image(models.Model):

    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images')
    description = models.TextField()
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    uploads_count = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username
