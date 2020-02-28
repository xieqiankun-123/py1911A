from rest_framework import viewsets
from .serializers import *
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import responses


class CategoryViewSets(viewsets.ModelViewSet):
    """
    分类视图
    继承 ModelViewSet 就可以拥有 HTTPS 协议的动词属性来了
    queryset = Category.objects.all()  指明操作的模型列表
    serializer_class = CategorySerializer 知名模型的序列化类
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class GoodViewSets(viewsets.ModelViewSet):
    """
    分类视图
    继承 ModelViewSet 就可以拥有 HTTPS 协议的动词属性来了
    queryset = Category.objects.all()  指明操作的模型列表
    serializer_class = CategorySerializer 知名模型的序列化类
    """
    queryset = Good.objects.all()
    serializer_class = GoodSerializer


class GoodImagesViewSets(viewsets.ModelViewSet):
    queryset = GoodImages.objects.all()
    serializer_class = GoodImageSerializer


@api_view(["GET", "POST"])
def category_list(request):
    if request.method == "GET":
        print("获取GET请求的参数为:", request.query_params)
        return HttpResponse("请求列表成功")
    elif request.method == "POST":
        print("获取POST请求的参数为:", request.date)
        return HttpResponse("创建成功")


@api_view(["GET", "PUT", "PATCH", "DELETE"])
def category_detail(request, c_id):
    if request.method == "GET":
        print("获取GET请求的参数为:", request.query_params)
        return HttpResponse("请求列表成功")
    elif request.method == "PUT" or request.method == "PATCH":
        print("获取PUT/PATCH请求的参数为:", request.data)
        return HttpResponse("创建成功")
    elif request.method == "DELETE":
        print("获取DELETE参数:")
        return HttpResponse("删除成功", request.data)
    else:
        return HttpResponse("当前路由不允许")
