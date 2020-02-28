from rest_framework import serializers
from .models import *


class GoodSerializer1(serializers.ModelSerializer):
    category = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = Good
        fields = ("id", "name", "desc", "category")


class CumentSerializer(serializers.RelatedField):
    def to_representation(self, value):
        return value.name + "+++++"


class CategorySerizlizer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField(max_length=10, min_length=1, error_messages={
        "max_length": "最多10个字",
        "min_length": "最少1个字",

    })
    goods = serializers.StringRelatedField(many=True, read_only=True)

    def create(self, validated_data):
        print("重写创建方法", validated_data)
        instance = Category.objects.create(**validated_data)
        return instance

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.save()
        return instance


class CategorySerializer1(serializers.ModelSerializer):
    """
    1.goods = serializers.StringRelatedField(many=True) 可以显示关联模型中的__str__的值
    2. = serializers.PrimaryKeyRelatedField(many=True, read_only=True)可以显示关联模型中的主键的值

    """

    # goods = serializers.StringRelatedField(many=True)

    # goods = GoodSerializer(many=True, read_only=True)
    goods = CumentSerializer(many=True, read_only=True)

    # goods = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # goods = serializers.HyperlinkedRelatedField(view_name='good-detail', many=True, read_only=True)
    # goods = serializers.SlugRelatedField(slug_field='name', many=True, read_only=True)

    class Meta:
        model = Category
        fields = ("name", "goods")


class GoodImageSerializer(serializers.Serializer):
    img = serializers.ImageField()
    # good = GoodSerializer()
    good = serializers.CharField(source='good.name')

    def validate(self, attrs):
        try:
            g = Good.objects.get(name=attrs["good"]["name"])
            attrs["good"] = g
        except:
            raise serializers.ValidationError("商品名不存在")

        return attrs

    def create(self, validated_data):
        instance = GoodImages.objects.create(**validated_data)
        return instance

    def update(self, instance, validated_data):
        instance.img = validated_data.get("name", instance.img)
        # instance.desc = validated_data.get("desc", instance.desc)
        instance.good = validated_data.get("good", instance.good)
        instance.save()
        return instance


# class GoodSerializer(serializers.Serializer):
#     # id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=10, min_length=3, error_messages={
#         "max_length": "最多10个字",
#         "min_length": "最少3个字"
#     })
#     category = CategorySerializer(label="分类")
#     imgs = GoodImageSerializer(label="图片", many=True, read_only=True)
#
#     # images = serializers.StringRelatedField(many=True, read_only=True)
#     def validate_category(self, category):
#         print("category原始数据:", category)
#         try:
#             Category.objects.get(name=category["name"])
#             print("处理后的category的值:", type(category))
#         except:
#             raise serializers.ValidationError("分类名不存在")
#         return category
#
#     def validate(self, attrs):
#         print("收到的数据为:", attrs)
#         try:
#             c = Category.objects.get(name=attrs["category"]["name"])
#         except:
#             c = Category.objects.create(name=attrs["category"]["name"])
#         attrs["category"] = c
#         return attrs
#
#     def create(self, validated_data):
#         print("+++", validated_data)
#         instance = Good.objects.create(**validated_data)
#         return instance
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get("name", instance.name)
#         # instance.desc = validated_data.get("desc", instance.desc)
#         instance.category = validated_data.get("category", instance.category)
#         instance.save()
#         return instance

class GoodSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20, min_length=2, error_messages={
        "max_length": "最多20个字",
        "min_length": "最少2个字"
    })
    category = CategorySerizlizer(label="分类")
    imgs = GoodImageSerializer(label="图片", many=True, read_only=True)

    def validate_category(self, category):
        """
        处理category
        :param category:  处理的原始值
        :return: 返回新值
        """
        print("category原始值为", category)
        try:
            Category.objects.get(name=category["name"])
        except:
            raise serializers.ValidationError("输入的分类名不存在")

        return category

    def validate(self, attrs):
        print("收到的数据为", attrs)
        try:
            c = Category.objects.get(name=attrs["category"]["name"])
        except:
            c = Category.objects.create(name=attrs["category"]["name"])
        attrs["category"] = c
        print("更改之后的数据", attrs)

        return attrs

    def create(self, validated_data):
        print("创建good参数", validated_data)
        instance = Good.objects.create(**validated_data)  # name=    category=
        return instance

    def update(self, instance, validated_data):
        print("原始值", instance.name, instance.category)
        instance.name = validated_data.get("name", instance.name)
        instance.category = validated_data.get("category", instance.category)
        instance.save()
        return instance
