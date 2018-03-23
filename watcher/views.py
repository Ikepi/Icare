from rest_framework import viewsets
# from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

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


#  类视图 使用viewset，
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class DeviceViewSet(viewsets.ModelViewSet):
    queryset = DeviceList.objects.all()
    serializer_class = DeviceListSerializer


class MapViewSet(viewsets.ModelViewSet):
    queryset = Map.objects.all()
    serializer_class = MapSerializer


class GyrViewSet(viewsets.ModelViewSet):
    queryset = Gyr.objects.all()
    serializer_class = GyrSerializer


class TempViewSet(viewsets.ModelViewSet):
    queryset = Temp.objects.all()
    serializer_class = TempSerializer


# 函数视图
# @api_view(['GET'])
# def get_id(request):
#     pass


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
        if device is None:
            queryset = Temp.objects.all()
            temp_serializer = TempSerializer(queryset, many=True, context={'request': request})
        else:
            try:
                queryset = Temp.objects.all().filter(device=device)[0]
            except IndexError:
                return Response(status=status.HTTP_404_NOT_FOUND)
            temp_serializer = TempSerializer(queryset, context={'request': request})
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
