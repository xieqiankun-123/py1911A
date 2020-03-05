from rest_framework import serializers
from .models import *


class DepartmentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=10, min_length=1, error_messages={
        "max_length": "最多10个字",
        "min_length": "最少1个字",

    })
    staff = serializers.StringRelatedField(many=True, read_only=True)

    def create(self, validated_data):
        print("重写创建方法", validated_data)
        instance = Department.objects.create(**validated_data)
        return instance

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.save()
        return instance


class StaffSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=10, min_length=1, error_messages={
        'max_length': "超过最大字数",
        'min_length': "未超过最少字数",
    })
    department = DepartmentSerializer(label="部门")

    def validate_department(self, department):
        print("category原始值为", department)
        try:
            Department.objects.get(name=department["name"])
        except:
            raise serializers.ValidationError("输入的分类名不存在")

        return department

    def validate(self, attrs):
        print("收到的数据为", attrs)
        try:
            c = Department.objects.get(name=attrs["department"]["name"])
        except:
            c = Department.objects.create(name=attrs["department"]["name"])
        attrs["department"] = c
        print("更改之后的数据", attrs)

        return attrs

    def create(self, validated_data):
        print("创建good参数", validated_data)
        instance = Staff.objects.create(**validated_data)  # name=    category=
        return instance

    def update(self, instance, validated_data):
        print("原始值", instance.name, instance.category)
        instance.name = validated_data.get("name", instance.name)
        instance.category = validated_data.get("category", instance.category)
        instance.save()
        return instance
