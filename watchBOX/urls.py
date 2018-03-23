"""watchBOX URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from watcher import views

admin.autodiscover()

router = routers.DefaultRouter()
router.register('user', views.UserViewSet)
router.register("gyr", views.GyrViewSet)
router.register("temp", views.TempViewSet)
router.register("map", views.MapViewSet)
router.register("devicelist", views.DeviceViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('temp-detail/', views.TempDetailView.as_view()),
    path('map-detail/', views.MapDetailView.as_view()),
    path('gyr-detail/', views.GyrDetailView.as_view()),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
"""
    path('home/', views.home_page),
    path('', views.home_page),
    path('sign_in/', views.sign_in_page),
    path('sign_up/', views.sign_up_page),
    path('login/', views.sign_in),
    path('register/', views.sign_up),
    path('logout/', views.sign_out),
"""
