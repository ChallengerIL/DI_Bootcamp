from django.urls import path
from . import views

urlpatterns = [
    path('people/<int:pk>/', views.person, name='person'),
    path('people/', views.people, name='people'),
]
