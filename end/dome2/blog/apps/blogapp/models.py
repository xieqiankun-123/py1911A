from django.db import models
from DjangoUeditor.models import UEditorField


# Create your models here.
class Ads(models.Model):
    img = models.ImageField(upload_to="ads", verbose_name="轮播图")
    desc = models.CharField(max_length=20, null=True, blank=True, verbose_name="图片描述")

    def __str__(self):
        return self.desc


class Category(models.Model):
    """
    定义分类模型类
    """
    name = models.CharField(max_length=50, verbose_name="分类名")

    def __str__(self):
        return self.name


class Tag(models.Model):
    """
    定义标签模型类
    """
    name = models.CharField(max_length=20, verbose_name="标签名")

    def __str__(self):
        return self.name


class Article(models.Model):
    """
    定义文章模型类
    """
    title = models.CharField(max_length=100, verbose_name="文章标题")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="所属分类")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    author = models.CharField(max_length=20, verbose_name="作者")
    views = models.IntegerField(default=0, verbose_name="浏览量")
    # body = models.TextField(verbose_name="正文")
    body = UEditorField(imagePath="img/", )
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title


class Comment(models.Model):
    name = models.CharField(max_length=20, default="jqk", verbose_name="姓名")
    url = models.URLField(default="http://www.jqk.com", verbose_name="个人主页")
    email = models.EmailField(default="286138163@qq.com", verbose_name="个人邮箱")
    body = models.CharField(max_length=500, verbose_name="评论内容")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="评论时间")
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name="所属文章")

    def __str__(self):
        return self.name
