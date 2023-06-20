from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='homepage'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', views.LoginPageView.as_view(), name='login'),
    path('profile/<pk>', views.ProfileView.as_view(), name='profile'),
    path('add-book/', views.BookCreateView.as_view(), name='add_book'),
    path('search/', views.BookSearchView.as_view(), name='search'),
    path('<slug>', views.BookDetailView.as_view(), name='book'),
]
