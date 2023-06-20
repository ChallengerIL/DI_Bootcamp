import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bike_store.settings")
import django

django.setup()

from rent.models import Rental, Vehicle, Customer
from faker import Faker
import random

fake = Faker()


while len(Rental.objects.all()) < 100:
    # Rental.objects.all().delete()
    # quit()

    vehicle = random.choice(Vehicle.objects.all())

    rental_date = fake.past_date()
    return_date = fake.past_date(start_date=rental_date)

    # Add random Nulls for the return date
    if random.randint(0, 1) == 1:
        return_date = None

    rental_list = Rental.objects.select_related('vehicle').filter(vehicle=vehicle.id)

    if len(rental_list) > 0:
        # Filter out all the unreturned vehicles
        if rental_list.filter(return_date__isnull=True).count() > 0:
            continue

        latest_rental = Rental.objects.select_related('vehicle').filter(vehicle=vehicle.id).latest('return_date')

        if latest_rental.return_date >= rental_date:
            continue

    rental = Rental(
        rental_date=rental_date,
        return_date=return_date,
        customer=random.choice(Customer.objects.all()),
        vehicle=vehicle,
    )
    rental.save()
