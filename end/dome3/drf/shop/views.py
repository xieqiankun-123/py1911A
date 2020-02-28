from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from .serializers import *
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response


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
        model = Category.objects.all()
        seria = CategorySerializer(instance=model, many=True)
        return Response(data=seria.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        seria = CategorySerializer(data=request.data)
        if seria.is_valid():
            seria.save()
            return Response(data=seria.data, status=status.HTTP_200_OK)
        else:
            return Response(data=seria.errors, status=status.HTTP_201_CREATED)


@api_view(["GET", "PUT", "PATCH", "DELETE"])
def category_detail(request, c_id):
    model = get_object_or_404(Category, pk=c_id)
    if request.method == "GET":
        seria = CategorySerializer(instance=model)
        return Response(data=seria.data, status=status.HTTP_200_OK)
    elif request.method == "PUT" or request.method == "PATCH":
        seria = CategorySerializer(instance=model, data=request.data)
        if seria.is_valid():
            seria.save()
            return Response(data=seria.data, status=status.HTTP_200_OK)
        else:
            return Response(data=seria.data, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        model.delete()
        return Response(status=status.HTTP_200_OK)
    else:
        return HttpResponse("当前路由不允许")


@api_view(["GET", "POST"])
def good_list(request):
    if request.method == "GET":
        seria = GoodSerializer(instance=Good.objects.all(), many=True)
        return Response(data=seria.data, status=status.HTTP_200_OK)
    if request.method == "POST":
        print("POST请求参数", request.data["category"])
        seria = GoodSerializer(data=request.data)
        if seria.is_valid():
            print("+++")
            seria.save()
            return Response(data=seria.data, status=status.HTTP_200_OK)
        else:
            return Response(data=seria.errors, status=status.HTTP_201_CREATED)


@api_view(["GET", "PUT", "PATCH", "DELETE"])
def good_detail(request, good_id):
    if request.method == "GET":
        return HttpResponse("获取数据成功")
    elif request.method == "PUT" or request.method == "PATCH":
        return HttpResponse("修改数据成功")
    elif request.method == "DELETE":
        return HttpResponse("删除数据成功")
