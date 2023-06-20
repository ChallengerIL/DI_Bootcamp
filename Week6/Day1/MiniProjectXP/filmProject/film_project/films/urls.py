from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='homepage'),
    path('add-film/', views.FilmCreateView.as_view(), name='add_film'),
    path('add-director/', views.DirectorCreateView.as_view(), name='add_director'),
]
