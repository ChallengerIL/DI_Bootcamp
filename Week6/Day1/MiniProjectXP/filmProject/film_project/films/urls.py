from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('add-film/', views.add_film, name='add_film'),
    path('add-director/', views.add_director, name='add_director'),
    # path('rent/rental/add', views.add_rental, name='add_rental'),
    # path('rent/customer/', views.all_customers, name='all_customers'),
    # path('rent/customer/<int:pk>', views.customer, name='customer'),
    # path('rent/customer/add', views.add_customer, name='add_customer'),
    # path('rent/vehicle/', views.all_vehicles, name='all_vehicles'),
    # path('rent/vehicle/<int:pk>', views.vehicle, name='vehicle'),
    # path('rent/vehicle/add', views.add_vehicle, name='add_vehicle'),
]
