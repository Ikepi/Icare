from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# 用户信息模型  auth.User


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
    n_s = models.IntegerField()
    w_e = models.IntegerField()
    time = models.DateTimeField(auto_now=True)
    device = models.OneToOneField(DeviceList, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.time)


# 体温
class Temp(models.Model):
    ta = models.CharField(max_length=10)  # 环境温度
    to = models.CharField(max_length=10)  # 目标温度
    time = models.DateTimeField(auto_now=True)
    device = models.ForeignKey(DeviceList, on_delete=models.CASCADE, related_name='temper')

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
    device = models.OneToOneField(DeviceList, on_delete=models.CASCADE)

    def __str__(self):
        return self.device
# 心电图
