from rest_framework import permissions

from wiremi.utils import check_user


class IsSuperUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.data.get('user_type') == 'IS_sSUPERUSER'


class IsAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        is_authenticated = check_user(request)
        if is_authenticated:
            return True
        return False


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        # Check if the user is authenticated and has user_type 'PM'
        return request.data.get('user_type') == 'IS_ADMIN'


class IsCustomer(permissions.BasePermission):
    def has_permission(self, request, view):
        # Check if the user is authenticated and has user_type 'PM'
        return request.data.get('user_type') == 'IS_CUSTOMER'
