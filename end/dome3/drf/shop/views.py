from rest_framework import viewsets
from .serializers import *


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
