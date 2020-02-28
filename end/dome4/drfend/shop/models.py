from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20, verbose_name="分类名")

    def __str__(self):
        return self.name


class Good(models.Model):
    name = models.CharField(max_length=20, verbose_name="商品名")
    desc = models.CharField(max_length=150, null=True, blank=True, verbose_name="商品描述")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="goods", verbose_name="商品分类")

    def __str__(self):
        return self.name


class GoodImgs(models.Model):
    img = models.ImageField(upload_to='good_img', verbose_name="商品展示图")
    good = models.ForeignKey(Good, on_delete=models.CASCADE, verbose_name="所属商品")
