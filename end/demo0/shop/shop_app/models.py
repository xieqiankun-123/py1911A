from django.db import models


# Create your models here.
class Ads(models.Model):
    """
    定义轮播图表
    """
    img = models.ImageField(upload_to='ads', verbose_name="轮播图片")
    desc = models.CharField(max_length=20, verbose_name="活动描述")

    def __str__(self):
        return self.desc


class GoodCategory(models.Model):
    """
    商品分类模型表

    """
    name = models.CharField(max_length=30, verbose_name="分类名")

    def __str__(self):
        return self.name


class Good(models.Model):
    """
    商品表
    """
    name = models.CharField(max_length=50, verbose_name="商品名")
    price = models.FloatField(default=0.0, verbose_name="商品价格")
    img = models.ImageField(upload_to='good_img', verbose_name="商品图片")
    desc = models.CharField(max_length=100, verbose_name="商品描述")
    category = models.ForeignKey(GoodCategory, on_delete=models.CASCADE, verbose_name="商品分类")

    def __str__(self):
        return self.name
