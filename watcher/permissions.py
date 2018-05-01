from rest_framework import permissions


class IsOwnerOrRefuse(permissions.BasePermission):
    """
    "自定义权限，只有设备的绑定者才能编辑设备信息"
    """
    def has_object_permission(self, request, view, obj):  # 访问对象时才会进行权限检测
        return obj.device_user.contains(request.user) or request.user.is_superuser

    def has_permission(self, request, view):  # 访问这个接口时，会进行权限检测
        if request.method in permissions.SAFE_METHODS or request.user.is_superuser:
            return True


class IsAdminOrWriteOnly(permissions.BasePermission):  # 针对用户管理
    def has_object_permission(self, request, view, obj):
        return obj == request.user or request.user.is_superuser
