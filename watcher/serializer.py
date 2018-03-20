from rest_framework import serializers
from watcher.models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    devicelist = serializers.HyperlinkedRelatedField(many=True, queryset=DeviceList.objects.all(), view_name="devicelist-detail")

    class Meta:
        model = User
        fields = ("url", "username", "email", "password", "devicelist")


class DeviceListSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(many=True, queryset=User.objects.all(), view_name="user-detail")

    class Meta:
        model = DeviceList
        fields = ("url", "number", "watchman", "fall_count", "user")


class MapSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Map
        fields = ("url", "n_s", "w_e", "time", "device")


class TemperatureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Temp
        fields = ("url", "ta", "to", "time", "device")


class GyrSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Gyr
        fields = ("url", "accx", "accy", "accz", "omegax",
                  "omegay", "omegaz", "anglex", "angley", "anglez", "fall", "device")
