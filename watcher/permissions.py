
from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    "自定义权限，只有设备的绑定者才能编辑设备信息"
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
            # Write permissions are only allowed to the owner of the snippet.
        return obj.device.user.all().include(request.user)
