from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("这里是应用的首页")


def about(request):
    return HttpResponse("这里是应用的关于页")
