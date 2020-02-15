from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=25, verbose_name="图书名", unique=True)
    price = models.FloatField(default=0, verbose_name="图书价格")
    bpub_date = models.DateField(default="1983-06-01")
    desc = models.CharField(max_length=30, null=True, blank=True, help_text="请输入图书的备注信息")

    def __str__(self):
        return self.title


class Hero(models.Model):
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=6, choices=(('male', '男'), ('female', "女")), default='male')
    content = models.CharField(max_length=100)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='heros')

    def __str__(self):
        return self.name


class UserManager(models.Manager):
    def delete_to_telephone(self, tele):
        user = self.get(telephone=tele)
        user.delete()

    def createUser(self, tele):
        user = self.model()
        user.telephone = tele
        user.save()


class User(models.Model):
    # name = models.CharField(max_length=20, verbose_name="姓名")
    telephone = models.CharField(max_length=11, null=True, blank=True, verbose_name="手机号码")
    objects = UserManager()

    def __str__(self):
        return self.telephone

    class Meta:
        # 数据库表名
        db_table = "用户表"
        ordering = ["telephone"]
        verbose_name = "用户模型表1"
        verbose_name_plural = "用户模型表2"


class Accont(models.Model):
    username = models.CharField(max_length=20, verbose_name="用户名")
    password = models.CharField(max_length=20, verbose_name="密码")
    regist_date = models.DateField(auto_now_add=True, verbose_name="注册日期")


class Concact(models.Model):
    telephone = models.CharField(max_length=11, verbose_name="手机号码")
    email = models.EmailField(default="2861358163@qq.com")
    accont = models.OneToOneField(Accont, on_delete=models.CASCADE)


class Artice(models.Model):
    title = models.CharField(max_length=20, verbose_name="文章标题")
    sumire = models.CharField(max_length=100, verbose_name="正文")


class Tag(models.Model):
    tag_name = models.CharField(max_length=30, verbose_name="标签名")
    artices = models.ManyToManyField(Artice,related_name="tags")
    pass
