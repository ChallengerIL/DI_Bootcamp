from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.student_list, name='students'),
    path('students/<pk>', views.student_detail, name='student'),
]
