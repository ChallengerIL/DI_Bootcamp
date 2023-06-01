import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bike_store.settings")
import django
django.setup()

from rent.models import RentalRate, VehicleSize, VehicleType

rate = 4.99

vehicle_sizes = VehicleSize.objects.all()
vehicle_types = VehicleType.objects.all()

for vehicle_type in vehicle_types:
    for vehicle_size in vehicle_sizes:
        rental_rate = RentalRate(
            daily_rate=rate,
            vehicle_type=vehicle_type,
            vehicle_size=vehicle_size,
        )
        rental_rate.save()
        rate += 1
