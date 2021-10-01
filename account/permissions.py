from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAccountOwnerPermission(BasePermission):

    def has_object_permission(self, request, view, obj):
        return bool(request.user == obj and request.method in SAFE_METHODS)