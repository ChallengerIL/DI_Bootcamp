from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('rent/rental/', views.all_rentals, name='all_rentals'),
    path('rent/rental/<int:pk>', views.rental, name='rental'),
    path('rent/rental/add', views.add_rental, name='add_rental'),
    path('rent/customer/<int:pk>', views.customer, name='customer'),
    path('rent/customer/add', views.add_customer, name='add_customer'),
    path('rent/vehicle/', views.all_vehicles, name='all_vehicles'),
    path('rent/vehicle/<int:pk>', views.vehicle, name='vehicle'),
    path('rent/vehicle/add', views.add_vehicle, name='add_vehicle'),
]
