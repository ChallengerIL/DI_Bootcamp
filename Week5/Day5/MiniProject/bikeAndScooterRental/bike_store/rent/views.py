from django.shortcuts import render, redirect
from .forms import CustomerForm, RentalForm, VehicleForm, check_availability
from .models import Rental, Customer, Vehicle
import datetime


def index(request):
    context = {
        'page_title': "Bike & Scooter Rental | Homepage",
    }
    return render(request, 'rent/index.html', context)


def all_rentals(request):
    context = {
        'title': "All Rentals",
        'rentals': Rental.objects.all(),
    }

    return render(request, 'rent/all_rentals.html', context)


def rental(request, pk):
    chosen_rental = Rental.objects.get(id=pk)

    if request.method == "POST":
        chosen_rental.return_date = datetime.datetime.now().date()
        chosen_rental.save()

    context = {
        'title': f'Rental #{chosen_rental.id}',
        'rental': chosen_rental,
    }

    return render(request, 'rent/rental.html', context)


def add_rental(request):
    if request.method == "POST":
        form = RentalForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("index")
    else:
        form = RentalForm()

    return render(request, 'rent/add_rental.html', {"form": form})


def customer(request, pk):
    chosen_customer = Customer.objects.get(id=pk)
    rentals = Rental.objects.filter(customer=chosen_customer)

    context = {
        'title': f"Customer {chosen_customer.first_name} {chosen_customer.last_name}",
        'customer': chosen_customer,
        'rentals': rentals,
    }

    return render(request, 'rent/customer.html', context)


def add_customer(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("index")
    else:
        form = CustomerForm()

    return render(request, 'rent/add_customer.html', {"form": form})


def all_vehicles(request):
    vehicles = Vehicle.objects.all()

    vehicles_dict = dict()

    for v in vehicles:
        vehicles_dict[v] = check_availability(v)

    context = {
        'title': 'All vehicles',
        'vehicles_dict': vehicles_dict,
    }

    return render(request, 'rent/all_vehicles.html', context)


def vehicle(request, pk):
    chosen_vehicle = Vehicle.objects.get(id=pk)

    context = {
        'title': f'Vehicle #{chosen_vehicle.id}',
        'vehicle': chosen_vehicle,
    }

    return render(request, 'rent/vehicle.html', context)


def add_vehicle(request):
    if request.method == "POST":
        form = VehicleForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("index")
    else:
        form = VehicleForm()

    return render(request, 'rent/add_vehicle.html', {"form": form})
