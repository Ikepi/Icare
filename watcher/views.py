from django.shortcuts import render
#from watcher.models import *
#from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.utils import json

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


#  类视图
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
    serializer_class = TemperatureSerializer


"""
@csrf_exempt  # 允许跨域访问
def test(request):
    if request.method == 'POST':
        value = request.body
        print(value)
        data = json.loads(value)
        print(data)

"""