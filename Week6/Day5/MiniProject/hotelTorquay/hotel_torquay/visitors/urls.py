from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('info/', views.InfoPageView.as_view(), name='info'),
    path('booking/', views.RoomsView.as_view(), name='booking'),
    path('order/<int:pk>', views.OrderView.as_view(), name='order'),
    path('contact/', views.contact, name='contact'),
]
