from django.core.exceptions import ValidationError
from django.db import models
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator


class Room(models.Model):

    class RoomType(models.IntegerChoices):
        SINGLE = 1
        DOUBLE = 2
        TRIPLE = 3
        QUAD = 4

    room_type = models.PositiveSmallIntegerField(
        choices=RoomType.choices,
        default=RoomType.SINGLE
    )
    price = models.IntegerField()
    room_number = models.IntegerField()

    def __str__(self):
        return f"Room #{self.room_number}"


class Booking(models.Model):
    guest = models.CharField(max_length=100)
    check_in = models.DateField()
    check_out = models.DateField()
    guests_num = models.IntegerField(
        validators=[
            MaxValueValidator(4),
            MinValueValidator(1)
        ]
    )
    room = models.ForeignKey(Room, related_name='booking', on_delete=models.CASCADE, blank=True)

    def check_availability(self):
        rooms = Room.objects.filter(room_type=self.guests_num)

        for room in rooms:
            self.room = room

            for booking in self.room.booking.all():
                if self.check_in > booking.check_in > self.check_out:
                    return True
                elif booking.check_out > self.check_in and booking.check_in < self.check_out:
                    return True
                elif booking.check_in < self.check_in and booking.check_out > self.check_out:
                    return True
        return False

    def clean(self):
        if self.check_in < datetime.date.today():
            raise ValidationError("The check in date cannot be in the past!")
        elif self.check_in >= self.check_out:
            raise ValidationError("The check out date have to come after the check in date!")
        elif self.check_availability():
            raise ValidationError("The date range you picked is not available!")

    def save(self, *args, **kwargs):
        super(Booking, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.guest}: {self.check_in} - {self.check_out}"


class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
