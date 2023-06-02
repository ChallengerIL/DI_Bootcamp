from django.db import models
from faker.providers import address
from phonenumber_field.modelfields import PhoneNumberField


class Customer(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = PhoneNumberField()
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class VehicleType(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class VehicleSize(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Vehicle(models.Model):

    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    vehicle_size = models.ForeignKey(VehicleSize, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    real_cost = models.IntegerField()

    def __str__(self):
        return f"{self.id} {self.vehicle_size} {self.vehicle_type}"


class Rental(models.Model):

    rental_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    customer = models.ForeignKey(Customer, related_name='customer', on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, related_name='vehicle', on_delete=models.CASCADE)

    def __str__(self):
        return f"Customer: {self.customer}, vehicle: {self.vehicle}, " \
               f"rental date: {self.rental_date}, " \
               f"return date: {self.return_date}"


class RentalRate(models.Model):

    daily_rate = models.DecimalField(decimal_places=2, max_digits=5)
    vehicle_type = models.ForeignKey(VehicleType, related_name='vehicle_type', on_delete=models.CASCADE)
    vehicle_size = models.ForeignKey(VehicleSize, related_name='vehicle_size', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.daily_rate} | {self.vehicle_type} | {self.vehicle_size}"


class Address(models.Model):

    address1 = models.CharField(max_length=300)
    address2 = models.CharField(max_length=300)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    postal_code = models.IntegerField()


class RentalStation(models.Model):

    name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    address = models.ForeignKey(Address, related_name='address', on_delete=models.CASCADE)
