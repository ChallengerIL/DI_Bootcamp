from django.urls import path
from . import views

urlpatterns = [
    path('', views.search, name='search'),
    path('persons/phonenumber/<str:phone>/', views.phone_number, name='phone_number'),
    path('persons/name/<str:persons_name>/', views.name, name='name'),
]
