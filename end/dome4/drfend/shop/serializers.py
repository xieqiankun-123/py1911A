from rest_framework import serializers
from .models import *


class GoodSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = Good
        fields = ("id", "name", "category")


class CategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=20, min_length=1, error_messages={
        "max_length": "最多20个字",
        "min_length": "最少1个字",
    })
    goods = serializers.SlugRelatedField(slug_field='name', many=True, read_only=True)

    class Meta:
        model = Category
        fields = ("id", "name", "goods")
