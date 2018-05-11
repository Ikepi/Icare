from django.core.cache import cache
from django.db.models.signals import pre_save
from django.dispatch import receiver
from rest_framework import status, generics
from rest_framework import viewsets, authentication, filters
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.utils import jwt_response_payload_handler

from watcher.permissions import *
from watcher.serializer import *

"""
# Create your views here.
def home_page(request):
    return render(request, "home.html")


def sign_in_page(request):
    return render(request, "sign_in.html")


def sign_up_page(request):
    return render(request, "sign_up.html")


def sign_out(request):
    logout(request)
    return render(request, 'home.html')


def sign_in(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)  # form 包含提交的数据
        if form.is_valid():  # 如果提交的数据合法
            input_username = form.cleaned_data['InputUserName']
            input_password = form.cleaned_data['InputPassword']
            user = authenticate(username=input_username, password=input_password)
            error_info = {}
            if user is not None:
                login(request, user)
                return render(request, 'workPage.html')
            else:
                error_info['error'] = 'User does not exist or Password error'
                return render(request, "sign_in.html", error_info)
    return render(request, "sign_in.html")


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            input_username = form.cleaned_data['InputUserName']
            input_password = form.cleaned_data['InputPassword']
            input_email = form.cleaned_data['InputEmail']
            input_confirmpassword = form.cleaned_data['InputConfirmPassword']
            error_info = {}
            if input_password != input_confirmpassword:
                error_info['error'] = 'Confirm password fail'
                return render(request, "sign_up.html", error_info)
            else:
                if User.objects.all().filter(username=input_username) is not None:
                    error_info['error'] = 'User name already exists'
                    return render(request, "sign_up.html", error_info)
                user = User.objects.create_user(input_username, input_email, input_password)
                user.save()
                login(request, user)
                return render(request, "workPage.html")
    return render(request, "sign_up.html")


# 激活设备
def activate_device(request):
    pass


# 接受传感器发来的定位信息
def accept_map(request):
    pass


# 接受传感器发来的体温
def temperature(request):
    pass
"""


class DefaultsMixin(object):  # 默认的配置
    authentication_class = (
        JSONWebTokenAuthentication,
        authentication.SessionAuthentication,
        authentication.BaseAuthentication,
    )
    permissions_classes = (
        permissions.IsAuthenticated
    )
    paginate = 25
    paginate_by_param = 'page_size'
    max_paginage_by = 100
    filter_backends = (
        filters.BaseFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    )  # 通过给每个viewset添加一个search_fields属性来设置SearchFilter，通过添加字段列表来设置OrderingFilter，
    # 让过滤器对添加的字段列表进行排序


#  类视图 使用viewset，
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminOrWriteOnly,)
    """
        Retrieve a model instance.
    """

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = UserDetailSerializer(instance, context={'request': request})
        return Response(serializer.data)

    def perform_create(self, serializer):
        return serializer.save()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # 判断用户名是否存在
        # username = serializer.validated_data['username']
        # try:
        #     User.objects.all().get(username=username)
        # except User.DoesNotExist:
        user = self.perform_create(serializer)
        # 生成token
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)

        headers = self.get_success_headers(serializer.data)
        # return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response(jwt_response_payload_handler(token), status=status.HTTP_201_CREATED, headers=headers)


class DeviceViewSet(viewsets.ModelViewSet):
    queryset = DeviceList.objects.all()
    serializer_class = DeviceListSerializer


class MapDetailViewSet(viewsets.ModelViewSet):
    queryset = MapDetail.objects.all()
    serializer_class = MapDetailSerializer
    permission_classes = (IsOwnerOrRefuse,)


class MapViewSet(viewsets.ModelViewSet):
    queryset = Map.objects.all()
    serializer_class = MapSerializer


class GyrDetailViewSet(viewsets.ModelViewSet):
    queryset = GyrDetail.objects.all()
    serializer_class = GyrDetailSerializer
    permission_classes = (IsOwnerOrRefuse,)


class GyrViewSet(viewsets.ModelViewSet):
    queryset = Gyr.objects.all()
    serializer_class = GyrSerializer

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #
    #     data = {'accx': request.data['accx'], 'accy': request.data['accy'], 'accz': request.data['accz'],
    #             'omegax': request.data['omegax'], 'omegay': request.data['omegay'], 'omegaz': request.data['omegaz'],
    #             'anglex': request.data['anglex'], 'angley': request.data['angley'], 'anglez': request.data['anglez'],
    #             'fall': request.data['fall'], 'device': request.data['device'], 'timestamp': request.data['timestamp']}
    #     gyr_detail_instance = GyrDetail.objects.filter(device=data['device']).select_related('device')
    #     if gyr_detail_instance.exists():
    #         detail_serializer = GyrDetailSerializer(gyr_detail_instance[0], data=data)
    #     else:
    #         detail_serializer = GyrDetailSerializer(data=data)
    #     detail_serializer.is_valid(raise_exception=True)
    #     detail_serializer.save()
    #
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class TempDetailViewSet(viewsets.ModelViewSet):
    queryset = TempDetail.objects.all()
    serializer_class = TempDetailSerializer
    permission_classes = (IsOwnerOrRefuse,)


class TempViewSet(viewsets.ModelViewSet):
    queryset = Temp.objects.all()
    serializer_class = TempSerializer
    lookup_field = 'id'

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #
    #     data = {'ta': request.data['ta'], 'to': request.data['to'], 'device': request.data['device'],
    #             'timestamp': request.data['timestamp']}
    #     temp_detail_instance = TempDetail.objects.filter(device=data['device']).select_related('device')
    #     if temp_detail_instance.exists():
    #         detail_serializer = TempDetailSerializer(temp_detail_instance[0], data=data)
    #     else:
    #         detail_serializer = TempDetailSerializer(data=data)
    #     detail_serializer.is_valid(raise_exception=True)
    #     detail_serializer.save()
    #
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class EcgAndRateViewSet(viewsets.ModelViewSet):
    queryset = EcgAndRate.objects.all()
    serializer_class = EcgAndRateSerializer


class EcgAndRateDetailViewSet(viewsets.ModelViewSet):
    queryset = EcgAndRateDetail.objects.all()
    serializer_class = EcgAndRateDetailSerializer
    permission_classes = (IsOwnerOrRefuse,)


class MapDetailWithRedis(generics.RetrieveAPIView):
    serializer_class = MapDetailSerializer

    def get_object(self):
        key = 'map_device_of_' + self.kwargs[self.lookup_field]
        obj = json.loads(cache.get(key))
        self.check_object_permissions(self.request, obj)
        
        return obj


@receiver(pre_save, sender=Map)
def update_before_map_save(sender, **kwargs):
    instance = kwargs['instance']
    instance_detail = MapDetail.objects.filter(device=instance.device_id).select_related('device')
    data = {'latitude': instance.latitude, 'longitude': instance.longitude,
            'device': instance.device_id, 'timestamp': instance.timestamp}
    if instance_detail.exists():
        serializer = MapDetailSerializer(instance_detail[0], data=data)
    else:
        serializer = MapDetailSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()

    # redis_data = json.dumps(MapDetail(latitude=instance.latitude, longitude=instance.longitude,
    #                                   device=instance.device_id, timestamp=instance.timestamp))
    # key = 'map_device_of_' + instance.device_id
    # cache.set(key, redis_data)


@receiver(pre_save, sender=Temp)
def update_before_temp_save(sender, **kwargs):
    instance = kwargs['instance']
    instance_detail = TempDetail.objects.filter(device=instance.device_id).select_related('device')
    data = {'ta': instance.ta, 'to': instance.to, 'device': instance.device_id, 'timestamp': instance.timestamp}
    if instance_detail.exists():
        serializer = TempDetailSerializer(instance_detail[0], data=data)
    else:
        serializer = TempDetailSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()


@receiver(pre_save, sender=Gyr)
def update_before_gyr_save(sender, **kwargs):
    instance = kwargs['instance']
    instance_detail = GyrDetail.objects.filter(device=instance.device_id).select_related('device')
    data = {'accx': instance.accx, 'accy': instance.accy, 'accz': instance.accz,
            'omegax': instance.omegax, 'omegay': instance.omegay, 'omegaz': instance.omegaz,
            'anglex': instance.anglex, 'angley': instance.angley, 'anglez': instance.anglez,
            'fall': instance.fall, 'device': instance.device_id, 'timestamp': instance.timestamp}
    if instance_detail.exists():
        serializer = GyrDetailSerializer(instance_detail[0], data=data)
    else:
        serializer = GyrDetailSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()


@receiver(pre_save, sender=EcgAndRate)
def update_before_gyr_save(sender, **kwargs):
    instance = kwargs['instance']
    instance_detail = EcgAndRateDetail.objects.filter(device=instance.device_id).select_related('device')
    data = {'ecgdata': instance.ecgdata, 'rate': instance.rate,
            'device': instance.device_id, 'timestamp': instance.timestamp}
    if instance_detail.exists():
        serializer = EcgAndRateDetailSerializer(instance_detail[0], data=data)
    else:
        serializer = EcgAndRateDetailSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()


"""
    # 需要注意的是，如果自己实现了get_object，需要使用self.check_object_permissions(self.request, obj)进行权限的检查。
    def get_object(self):
        def get_queryset():
            return TempDetail.objects.all()
        queryset = get_queryset()
        filter = {}
        field = self.lookup_field
        filter[field] = self.kwargs[field]
        obj = get_object_or_404(queryset, **filter)
        self.check_object_permissions(self.request, obj)
        return obj
"""
"""
# 重写源码后，以下方法可以不用
# app获取数据使用“http://172.26.19.220:8000/xxx/?device=设备号”的形式

# 获取设备号device
def get_device(request):
    device = request.GET.get('device')
    return device


# 使用类视图
class TempDetailView(APIView):
    # permission_classes = () # 为判断是否有权限访问这个设备的数据
    # permission_classes = AllowAny

    @staticmethod
    def get(request):
        device = get_device(request)
        print(device)
        if device is None:
            queryset = TempDetail.objects.all()
            temp_serializer = TempDetailSerializer(queryset, many=True, context={'request': request})
        else:
            try:
                queryset = TempDetail.objects.all().filter(device=device)[0]
                print(queryset)
            except IndexError:
                return Response(status=status.HTTP_404_NOT_FOUND)
            temp_serializer = TempDetailSerializer(queryset, context={'request': request})
        return Response(temp_serializer.data)


# 使用类视图
class GyrDetailView(APIView):
    # permission_classes = () # 为判断是否有权限访问这个设备的数据
    # permission_classes = AllowAny

    @staticmethod
    def get(request):
        device = get_device(request)
        if device is None:
            queryset = Gyr.objects.all()
            gyr_serializer = GyrSerializer(queryset, many=True, context={'request': request})
        else:
            try:
                queryset = Gyr.objects.all().filter(device=device)[0]
            except IndexError:
                return Response(status=status.HTTP_404_NOT_FOUND)
            gyr_serializer = GyrSerializer(queryset, context={'request': request})
        return Response(gyr_serializer.data)


class MapDetailView(APIView):
    # permission_classes = () # 为判断是否有权限访问这个设备的数据
    # permission_classes = AllowAny

    @staticmethod
    def get(request):
        device = get_device(request)
        if device is None:
            queryset = Map.objects.all()
            map_serializer = MapSerializer(queryset, many=True, context={'request': request})
        else:
            try:
                queryset = Map.objects.all().filter(device=device)[0]
            except IndexError:
                return Response(status=status.HTTP_404_NOT_FOUND)
            map_serializer = MapSerializer(queryset, context={'request': request})
        return Response(map_serializer.data)
"""
