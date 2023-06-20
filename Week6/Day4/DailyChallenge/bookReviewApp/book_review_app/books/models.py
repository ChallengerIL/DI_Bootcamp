from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg
from django.utils.text import slugify
from django.db.models.signals import post_save


class Book(models.Model):

    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(null=True)
    author = models.CharField(max_length=50)
    published_date = models.DateField()
    description = models.TextField()
    page_count = models.IntegerField()
    categories = models.CharField(max_length=200)
    thumbnail_url = models.URLField()

    rating = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Book, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class BookReview(models.Model):

    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    rating = models.IntegerField()
    review_text = models.TextField()

    def __str__(self):
        return f"{self.user}: {self.review_text[:30]}"


def post_review_added_signal(sender, instance, created, **kwargs):
    book = Book.objects.get(id=instance.book.id)
    reviews = book.reviews.all()

    book.rating = reviews.aggregate(Avg('rating'))['rating__avg']
    book.save()


post_save.connect(receiver=post_review_added_signal, sender=BookReview)

