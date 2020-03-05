from rest_framework import permissions


class OrderPermissions(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        print("++++", request.user, obj.user)
        return request.user == obj.user
