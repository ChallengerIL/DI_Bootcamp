from django.urls import path
from . import views
# from .views import SignUpView

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('profile/', views.profile, name='profile'),
]
