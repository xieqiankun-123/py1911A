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


class CategorySerializer(serializers.Serializer):
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


class GoodSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=10, min_length=3, error_messages={
        "max_length": "最多10个字",
        "min_length": "最少3个字"
    })
    desc = serializers.CharField(max_length=150, error_messages={
        "max_length": "商品的描述最多为150个字",

    })
    category = CategorySerializer()
    goodimage = serializers.HyperlinkedRelatedField(view_name='goodimages-detail', many=True, read_only=True)

    # images = serializers.StringRelatedField(many=True, read_only=True)
    def validate_category(self, category):
        print("category原始数据:", category)
        try:
            Category.objects.get(name=category["name"])
            print("处理后的category的值:", type(category))

        except:
            raise serializers.ValidationError("分类名不存在")
        return category

    def validate(self, attrs):
        print("收到的数据为:", attrs)
        try:
            c = Category.objects.get(name=attrs["category"]["name"])
        except:
            c = Category.objects.create(name=attrs["category"]["name"])
        attrs["category"] = c
        return attrs

    def create(self, validated_data):
        print("+++", validated_data)
        instance = Good.objects.create(**validated_data)

        return instance

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.desc = validated_data.get("desc", instance.desc)
        instance.save()
        return instance


class GoodImageSerializer(serializers.Serializer):
    img = serializers.ImageField()
    good = GoodSerializer()

    def validate(self, attrs):
        try:
            g = Good.objects.get(name=attrs["good"]["name"])
        except:
            raise serializers.ValidationError("商品名不存在")

        attrs["good"] = g
        return attrs

    def create(self, validated_data):
        instance = GoodImages.objects.create(**validated_data)
        return instance

    def update(self, instance, validated_data):
        instance.img = validated_data.get("name", instance.img)
        # instance.desc = validated_data.get("desc", instance.desc)
        instance.save()
        return instance
