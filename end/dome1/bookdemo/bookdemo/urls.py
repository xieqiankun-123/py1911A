"""bookdemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include
from django.http import HttpResponse


def index(request):
    return HttpResponse("这里是首页")


def list(request):
    return HttpResponse("这里是列表页")


def jsondata(request):
    return HttpResponse("{'name':'解乾坤','age':'20','sex':'男'}")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('booktest/',include('booktest.urls')),
    path('json/', jsondata),
    path('index/', index),
    path('list/', list)
]
