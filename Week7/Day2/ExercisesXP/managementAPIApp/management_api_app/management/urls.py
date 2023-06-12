from django.urls import path
from .views import *

urlpatterns = [
    path('departments/', DepartmentListAPIView.as_view(), name='departments_list'),
    path('departments/create/', DepartmentCreateAPIView.as_view(), name='departments_create'),
    path('employees/', EmployeeListAPIView.as_view(), name='employees_list'),
    path('employees/create/', EmployeeCreateAPIView.as_view(), name='employees_create'),
    path('projects/<int:pk>/', ProjectRetrieveAPIView.as_view(), name='projects_retrieve'),
    path('projects/<int:pk>/update/', ProjectUpdateAPIView.as_view(), name='projects_update'),
    path('projects/<int:pk>/delete/', ProjectDestroyAPIView.as_view(), name='projects_delete'),
    path('tasks/<int:pk>/', TaskRetrieveAPIView.as_view(), name='tasks_retrieve'),
    path('tasks/<int:pk>/update/', TaskUpdateAPIView.as_view(), name='tasks_update'),
    path('tasks/<int:pk>/delete/', TaskDestroyAPIView.as_view(), name='tasks_delete'),
]
