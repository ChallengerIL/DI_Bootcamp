from rest_framework.permissions import BasePermission
from .models import DepartmentAdmin


class IsDepartmentAdmin(BasePermission):

    def has_permission(self, request, user):
        return hasattr(request.user, 'departmentadmin')


















