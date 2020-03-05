from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status, generics, mixins, filters
from rest_framework.views import APIView

from .serializers import *
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
# from rest_framework import permissions
from .permissions import *
# from rest_framework.throttling import *
from .throttling import MyAnon, MyUser
from .pagination import *

from django_filters.rest_framework import DjangoFilterBackend


class CategoryViewSets2(viewsets.ModelViewSet):
    """
    分类视图
    继承 ModelViewSet 就可以拥有 HTTPS 协议的动词属性来了
    queryset = Category.objects.all()  指明操作的模型列表
    serializer_class = CategorySerializer 知名模型的序列化类
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @action(methods=["GET"], detail=False)
    def getlactscategory(self, request):
        num = int(request.query_params.get("num", 0))
        print(num)
        seria = CategorySerializer(instance=Category.objects.all()[:num], many=True)
        return Response(data=seria.data, status=status.HTTP_200_OK)


class CategoryViewSets(viewsets.ModelViewSet):
    """
    分类视图
    继承 ModelViewSet 就可以拥有 HTTPS 协议的动词属性来了
    queryset = Category.objects.all()  指明操作的模型列表
    serializer_class = CategorySerializer 知名模型的序列化类
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    # permission_classes = [permissions.IsAdminUser]

    def get_permissions(self):
        if self.action == "create" or self.action == "update" or self.action == "partial_update" or self.action == "destroy":
            return [permissions.IsAdminUser()]
        else:
            return []

    # 使用自定义的频次限制类
    throttle_classes = [MyAnon, MyUser]
    # 使用自定义的分类器类
    # pagination_class = MyPageNumberPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["name"]
    search_fields = ["name"]
    ordering_fields = ["id"]


class OrderViewSets(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    # permission_classes = [permissions.IsAuthenticated]
    def get_permissions(self):

        if self.action == "partial_update" or self.action == "update" or self.action == "retrieve" or self.action == "destroy":
            return [OrderPermissions()]
        elif self.action == "create":
            return [permissions.IsAuthenticated()]
        else:
            return [permissions.IsAdminUser()]


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
    serializer_class = CategorySerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class CategoryDetailView2(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                          mixins.DestroyModelMixin):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

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
        seria = CategorySerializer(instance=Category.objects.all(), many=True)
        return Response(data=seria.data, status=status.HTTP_200_OK)

    def post(self, request):
        seria = CategorySerializer(data=request.data)
        seria.is_valid(raise_exception=True)
        seria.save()
        return Response(data=seria.data, status=status.HTTP_201_CREATED)


# class GoodListView1(APIView):
#     def get(self, request):
#         seria = GoodSerializer(instance=Good.objects.all(), many=True)
#         return Response(data=seria.data, status=status.HTTP_200_OK)
#
#     def post(self, request):
#         seria = GoodSerializer(data=request.data)
#         seria.is_valid(raise_exception=True)
#         seria.save()
#         return Response(data=seria.data, status=status.HTTP_201_CREATED)


class CategoryDetailView1(APIView):
    def get(self, request, c_id):
        seria = CategorySerializer(instance=get_object_or_404(Category, pk=c_id))
        return Response(data=seria.data, status=status.HTTP_200_OK)

    def put(self, request, c_id):
        seria = CategorySerializer(instance=get_object_or_404(Category, pk=c_id), data=request.data)
        seria.is_valid(raise_exception=True)
        seria.save()
        return Response(data=seria.data, status=status.HTTP_200_OK)

    def patch(self, request, c_id):
        seria = CategorySerializer(instance=get_object_or_404(Category, pk=c_id), data=request.data)
        seria.is_valid(raise_exception=True)
        seria.save()
        return Response(data=seria.data, status=status.HTTP_200_OK)

    def delete(self, request, c_id):
        get_object_or_404(Category, pk=c_id).delete()
        return Response(status=status.HTTP_200_OK)


class CategoryListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


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

class UserViewSets1(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(methods=["POST"], detail=False)
    def regist(self, request):
        seria = UserRegistSerializer(data=request.data)
        seria.is_valid(raise_exception=True)
        seria.save()
        return Response("注册成功", status=status.HTTP_200_OK)


class UserViewSets(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin):
    """
    定义用户视图类
    """
    queryset = User.objects.all()

    # serializer_class = UserSerializer

    def get_serializer_class(self):
        print("请求的方法为:", self.action)
        if self.action == "create":
            return UserRegistSerializer
        else:
            return UserSerializer
