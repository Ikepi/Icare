# from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
# from django.db.models.signals import post_save
# from django.dispatch import receiver
from django.utils import timezone
from rest_framework.authtoken.models import Token


# Create your models here.
# 用户信息模型  auth.User

# class User(AbstractUser):  # 自定义用户模型
#     nickname = models.CharField(max_length=50, blank=True)
#
#     class Meta(AbstractUser.Meta):
#         pass

# 普通token认证，用JSON Web Token就不需要了
# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)


# 设备列表
class DeviceList(models.Model):
    number = models.CharField(primary_key=True, max_length=10)  # SIM卡卡号,主键
    watchman = models.CharField(max_length=10)
    fall_count = models.IntegerField(default=0)
    user = models.ManyToManyField(User, related_name="devicelist")
    password = models.CharField(max_length=10)  # SIM卡密码

    def __str__(self):
        return self.number

    def user_list(self):
        return ','.join([i.username for i in self.user.all()])


# 定位信息模型
class Map(models.Model):
    latitude = models.CharField(max_length=8)
    longitude = models.CharField(max_length=8)
    time = models.TimeField(auto_now=True)
    device = models.ForeignKey(DeviceList, on_delete=models.CASCADE, related_name='map')
    timestamp = models.TimeField()

    def __str__(self):
        return str(self.time)

    class Meta:
        ordering = ['id']


class MapDetail(models.Model):
    latitude = models.CharField(max_length=8)
    longitude = models.CharField(max_length=8)
    time = models.TimeField(auto_now=True)
    device = models.OneToOneField(DeviceList, on_delete=models.CASCADE, related_name='map_detail', primary_key=True)
    timestamp = models.TimeField()

    def __str__(self):
        return str(self.time)


# 体温
class Temp(models.Model):
    ta = models.CharField(max_length=10)  # 环境温度
    to = models.CharField(max_length=10)  # 目标温度
    time = models.TimeField(auto_now=True)
    device = models.ForeignKey(DeviceList, on_delete=models.CASCADE, related_name='temper')
    timestamp = models.TimeField()

    def __str__(self):
        return str(self.time)

    class Meta:
        ordering = ['id']


# 保存最新的体温信息，提高获取速度，以达到app实时的效果
class TempDetail(models.Model):
    ta = models.CharField(max_length=10)  # 环境温度
    to = models.CharField(max_length=10)  # 目标温度
    time = models.TimeField(auto_now=True)
    device = models.OneToOneField(DeviceList, on_delete=models.CASCADE, related_name='temper_detail', primary_key=True)
    timestamp = models.TimeField()

    def __str__(self):
        return str(self.time)


class Gyr(models.Model):  # 陀螺仪数据
    accx = models.CharField(max_length=25)
    accy = models.CharField(max_length=25)
    accz = models.CharField(max_length=25)
    omegax = models.CharField(max_length=25)
    omegay = models.CharField(max_length=25)
    omegaz = models.CharField(max_length=25)
    anglex = models.CharField(max_length=25)
    angley = models.CharField(max_length=25)
    anglez = models.CharField(max_length=25)
    fall = models.BooleanField()
    device = models.ForeignKey(DeviceList, on_delete=models.CASCADE, related_name='gyr')
    timestamp = models.TimeField()
    time = models.TimeField(auto_now=True)

    def __str__(self):
        return self.device

    class Meta:
        ordering = ['id']


class GyrDetail(models.Model):  # 陀螺仪数据
    accx = models.CharField(max_length=25)
    accy = models.CharField(max_length=25)
    accz = models.CharField(max_length=25)
    omegax = models.CharField(max_length=25)
    omegay = models.CharField(max_length=25)
    omegaz = models.CharField(max_length=25)
    anglex = models.CharField(max_length=25)
    angley = models.CharField(max_length=25)
    anglez = models.CharField(max_length=25)
    fall = models.BooleanField()
    device = models.OneToOneField(DeviceList, on_delete=models.CASCADE, related_name='gyr_detail', primary_key=True)
    timestamp = models.TimeField()
    time = models.TimeField(auto_now=True)

    def __str__(self):
        return self.device

# 心电图
