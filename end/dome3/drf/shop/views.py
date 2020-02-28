from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status, generics, mixins
from rest_framework.views import APIView

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
    serializer_class = CategorySerizlizer


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


class CategoryListView2(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Category.objects.all()
    serializer_class = CategorySerizlizer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class CategoryDetailView2(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                          mixins.DestroyModelMixin):
    queryset = Category.objects.all()
    serializer_class = CategorySerizlizer

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def patch(self, request, pk):
        return self.partial_update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)


class CategoryListView1(APIView):
    def get(self, request):
        seria = CategorySerizlizer(instance=Category.objects.all(), many=True)
        return Response(data=seria.data, status=status.HTTP_200_OK)

    def post(self, request):
        seria = CategorySerizlizer(data=request.data)
        seria.is_valid(raise_exception=True)
        seria.save()
        return Response(data=seria.data, status=status.HTTP_201_CREATED)


class CategoryDetailView1(APIView):
    def get(self, request, c_id):
        seria = CategorySerizlizer(instance=get_object_or_404(Category, pk=c_id))
        return Response(data=seria.data, status=status.HTTP_200_OK)

    def put(self, request, c_id):
        seria = CategorySerizlizer(instance=get_object_or_404(Category, pk=c_id), data=request.data)
        seria.is_valid(raise_exception=True)
        seria.save()
        return Response(data=seria.data, status=status.HTTP_200_OK)

    def patch(self, request, c_id):
        seria = CategorySerizlizer(instance=get_object_or_404(Category, pk=c_id), data=request.data)
        seria.is_valid(raise_exception=True)
        seria.save()
        return Response(data=seria.data, status=status.HTTP_200_OK)

    def delete(self, request, c_id):
        get_object_or_404(Category, pk=c_id).delete()
        return Response(status=status.HTTP_200_OK)


class CategoryListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerizlizer


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerizlizer


# class GoodListView(generics.ListCreateAPIView):
#     queryset = Good.objects.all()
#     serializer_class = GoodSerializer

class GoodViewSets1(viewsets.ModelViewSet):
    queryset = Good.objects.all()
    serializer_class = GoodSerializer


@api_view(["GET", "POST"])
def category_list(request):
    if request.method == "GET":
        model = Category.objects.all()
        seria = CategorySerizlizer(instance=model, many=True)
        return Response(data=seria.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        seria = CategorySerizlizer(data=request.data)
        if seria.is_valid():
            seria.save()
            return Response(data=seria.data, status=status.HTTP_200_OK)
        else:
            return Response(data=seria.errors, status=status.HTTP_201_CREATED)


@api_view(["GET", "PUT", "PATCH", "DELETE"])
def category_detail(request, c_id):
    model = get_object_or_404(Category, pk=c_id)
    if request.method == "GET":
        seria = CategorySerizlizer(instance=model)
        return Response(data=seria.data, status=status.HTTP_200_OK)
    elif request.method == "PUT" or request.method == "PATCH":
        seria = CategorySerizlizer(instance=model, data=request.data)
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

# @api_view(["GET", "POST"])
# def good_list(request):
#     if request.method == "GET":
#         seria = GoodSerializer(instance=Good.objects.all(), many=True)
#         return Response(data=seria.data, status=status.HTTP_200_OK)
#     if request.method == "POST":
#         print("POST请求参数", request.data["category"])
#         seria = GoodSerializer(data=request.data)
#         if seria.is_valid():
#             print("+++")
#             seria.save()
#             return Response(data=seria.data, status=status.HTTP_200_OK)
#         else:
#             return Response(data=seria.errors, status=status.HTTP_201_CREATED)


# @api_view(["GET", "PUT", "PATCH", "DELETE"])
# def good_detail(request, good_id):
#     if request.method == "GET":
#         return HttpResponse("获取数据成功")
#     elif request.method == "PUT" or request.method == "PATCH":
#         return HttpResponse("修改数据成功")
#     elif request.method == "DELETE":
#         return HttpResponse("删除数据成功")
