from django.contrib import admin
from . import models

admin.site.register(models.Customer)
admin.site.register(models.VehicleType)
admin.site.register(models.VehicleSize)
admin.site.register(models.Vehicle)
admin.site.register(models.Rental)
admin.site.register(models.RentalRate)
