from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    """
    1.goods = serializers.StringRelatedField(many=True) 可以显示关联模型中的__str__的值
    2. = serializers.PrimaryKeyRelatedField(many=True, read_only=True)可以显示关联模型中的主键的值

    """

    # goods = serializers.StringRelatedField(many=True)
    # goods = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    goods = serializers.HyperlinkedRelatedField(view_name='good-detail', many=True, read_only=True)

    class Meta:
        model = Category
        fields = "__all__"


class GoodSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = Good
        fields = "__all__"
