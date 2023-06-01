import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bike_store.settings")
import django
django.setup()

from rent.models import Customer
from faker import Faker

fake = Faker()

for k in range(1000):
    customer = Customer(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        email=fake.email(safe=True),
        phone_number=fake.phone_number(),
        address=fake.address(),
        city=fake.city(),
        country=fake.country(),
    )
    customer.save()
