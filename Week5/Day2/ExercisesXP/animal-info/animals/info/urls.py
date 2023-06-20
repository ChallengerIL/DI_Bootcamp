from django.urls import path
from . import views

urlpatterns = [
    path('family/<int:pk>/', views.family, name='family'),
    path('animal/<int:pk>/', views.animal, name='animal'),
    path('animals/', views.animals, name='animals'),
]
