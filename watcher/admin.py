from django.contrib import admin
# from rest_framework.authtoken.admin import TokenAdmin

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
admin.site.register(TempDetail)
admin.site.register(MapDetail)
admin.site.register(GyrDetail)

# 也可以通过管理界面手动创建令牌。如果你使用的是大型用户群，我们建议你动态修改TokenAdmin类，
# 以根据你的需要进行自定义，更具体地说，将user字段声明为raw_field。
# TokenAdmin.raw_id_fields = ('user',)
