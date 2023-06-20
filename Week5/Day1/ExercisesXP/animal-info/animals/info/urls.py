from django.urls import path
from . import views

urlpatterns = [
    path('animal/<int:pk>/', views.animal, name='animal'),
    path('family/<int:pk>/', views.family, name='family'),
]
