import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hotel_torquay.settings")
import django
django.setup()
from visitors.models import Booking, Room
from datetime import datetime, timedelta
from faker import Faker
import random
from django.core.exceptions import ValidationError

BOOKINGS_TOTAL = 500
MAX_PERIOD = 14

while BOOKINGS_TOTAL > 0:
    # Booking.objects.all().delete()
    # quit()

    fake = Faker()
    tomorrow = datetime.now() + timedelta(1)
    check_in = fake.date_between(start_date=tomorrow, end_date=tomorrow + timedelta(365))
    check_out = check_in + timedelta(random.randint(1, MAX_PERIOD))
    # room = random.choice(Room.objects.all())
    # booking_list = Booking.objects.select_related('room').filter(room=room.id)

    booking = Booking(
        guest=fake.name(),
        check_in=check_in,
        check_out=check_out,
        guests_num=random.randint(1, 4),
        # room=room,
    )

    try:
        booking.full_clean()
    except ValidationError:
        continue
    else:
        BOOKINGS_TOTAL -= 1
