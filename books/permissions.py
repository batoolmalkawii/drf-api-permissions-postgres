from rest_framework import permissions

class PermissionsClass(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.id == 1:
            return True
        if request.method == 'DELETE' and obj.author != request.user:
            return False        
        if request.method in permissions.SAFE_METHODS:
            return True
        if obj.author == request.user:
            return True

