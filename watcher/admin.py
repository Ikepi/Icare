from django.contrib import admin
from watcher.models import *
# Register your models here.


class DeviceListAdmin(admin.ModelAdmin):
    list_display = ("number", "watchman", "fall_count", "user_list")


class MapAdmin(admin.ModelAdmin):
    list_display = ()


class TempAdmin(admin.ModelAdmin):
    list_display = ()


admin.site.register(DeviceList, admin_class=DeviceListAdmin)
admin.site.register(Map)
admin.site.register(Temp)
admin.site.register(Gyr)
