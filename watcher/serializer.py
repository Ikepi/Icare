import traceback

from rest_framework import serializers
from rest_framework.serializers import raise_errors_on_nested_writes
from rest_framework.utils import model_meta

from watcher.models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    devicelist = serializers.HyperlinkedRelatedField(many=True, queryset=DeviceList.objects.all(),
                                                     view_name="devicelist-detail", write_only=True)

    class Meta:
        model = User
        fields = ("url", "id", "username", "password", "email", "devicelist")
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'write_only': True},
        }

    def create(self, validated_data):
        raise_errors_on_nested_writes('create', self, validated_data)
        ModelClass = self.Meta.model
        info = model_meta.get_field_info(ModelClass)
        many_to_many = {}
        for field_name, relation_info in info.relations.items():
            if relation_info.to_many and (field_name in validated_data):
                many_to_many[field_name] = validated_data.pop(field_name)
        try:
            # instance = ModelClass.objects.create(**validated_data)
            user = User.objects.create(
                username=validated_data['username'],
                email=validated_data['email'],
            )
            user.set_password(validated_data['password'])
        except TypeError:
            tb = traceback.format_exc()
            msg = (
                'Got a `TypeError` when calling `%s.objects.create()`. '
                'This may be because you have a writable field on the '
                'serializer class that is not a valid argument to '
                '`%s.objects.create()`. You may need to make the field '
                'read-only, or override the %s.create() method to handle '
                'this correctly.\nOriginal exception was:\n %s' %
                (
                    ModelClass.__name__,
                    ModelClass.__name__,
                    self.__class__.__name__,
                    tb
                )
            )
            raise TypeError(msg)

            # Save many-to-many relationships after the instance is created.
        if many_to_many:
            for field_name, value in many_to_many.items():
                field = getattr(user, field_name)
                field.set(value)
        user.save()
        return user

    def update(self, instance, validated_data):
        # raise_errors_on_nested_writes('update', self, validated_data)
        info = model_meta.get_field_info(instance)
        for attr, value in validated_data.items():
            if attr in info.relations and info.relations[attr].to_many:
                field = getattr(instance, attr)
                field.set(value)
        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('username', instance.username)
        password_temp = validated_data.get('password', instance.password)
        if password_temp != instance.password:
            instance.set_password(password_temp)
        instance.save()
        return instance


class UserDetailSerializer(serializers.HyperlinkedModelSerializer):
    devicelist = serializers.HyperlinkedRelatedField(many=True, queryset=DeviceList.objects.all(),
                                                     view_name="devicelist-detail")

    class Meta:
        model = User
        fields = ("url", "id", "username", "password", "email", "devicelist")


class DeviceListSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(many=True, queryset=User.objects.all(), view_name="user-detail")

    class Meta:
        model = DeviceList
        fields = ("url", "number", "watchman", "fall_count", "user")


class MapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Map
        fields = ("url", "id", "latitude", "longitude", "time", "device", "timestamp")


class MapDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = MapDetail
        fields = ("url", "latitude", "longitude", "time", "device", "timestamp")


class TempSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temp
        fields = ("url", "id", "ta", "to", "time", "device", "timestamp")
        extra_kwargs = {
            'url': {'view_name': 'temp-detail', 'lookup_field': 'id'},
            # 'device': {'lookup_field': 'username'}
        }


class TempDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = TempDetail
        fields = ("url", "ta", "to", "time", "device", "timestamp")


class GyrSerializer(serializers.ModelSerializer):
    # device = serializers.ReadOnlyField(source="device.number")

    class Meta:
        model = Gyr
        fields = ("url", "id", "accx", "accy", "accz", "omegax",
                  "omegay", "omegaz", "anglex", "angley", "anglez", "fall", "device", "time", "timestamp")


class GyrDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = GyrDetail
        fields = ("url", "accx", "accy", "accz", "omegax",
                  "omegay", "omegaz", "anglex", "angley", "anglez", "fall", "device", "time", "timestamp")
