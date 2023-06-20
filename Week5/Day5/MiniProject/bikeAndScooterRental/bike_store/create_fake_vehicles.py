import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bike_store.settings")
import django
django.setup()

from rent.models import Vehicle, VehicleType, VehicleSize
import random

for k in range(300):
    vehicle = Vehicle(
        vehicle_type=random.choice(VehicleType.objects.all()),
        vehicle_size=random.choice(VehicleSize.objects.all()),
        real_cost=random.randint(500, 10000),
    )
    vehicle.save()
