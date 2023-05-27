from rest_framework.permissions import BasePermission
from users.models import UserRoles


class IsAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.role == UserRoles.ADMIN


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user
