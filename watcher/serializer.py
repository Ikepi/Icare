from rest_framework import serializers
from watcher.models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    devicelist = serializers.HyperlinkedRelatedField(many=True, queryset=DeviceList.objects.all(),
                                                     view_name="devicelist-detail")

    class Meta:
        model = User
        fields = ("url", "username", "email", "devicelist")


class DeviceListSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(many=True, queryset=User.objects.all(), view_name="user-detail")

    class Meta:
        model = DeviceList
        fields = ("url", "number", "watchman", "fall_count", "user")


class MapSerializer(serializers.HyperlinkedModelSerializer):
    # device = serializers.ReadOnlyField(source="device.number")

    class Meta:
        model = Map
        fields = ("url", "n_s", "w_e", "time", "device")


class TempSerializer(serializers.HyperlinkedModelSerializer):
    # device = serializers.ReadOnlyField(source="device.number")

    class Meta:
        model = Temp
        fields = ("url", "ta", "to", "time", "device")


class GyrSerializer(serializers.HyperlinkedModelSerializer):
    # device = serializers.ReadOnlyField(source="device.number")

    class Meta:
        model = Gyr
        fields = ("url", "id", "accx", "accy", "accz", "omegax",
                  "omegay", "omegaz", "anglex", "angley", "anglez", "fall", "device")
