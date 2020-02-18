from django.db import models

from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    """
    自定义用户类

    """
    telephone = models.CharField(max_length=11,verbose_name="手机号")
    votes = models.ManyToManyField('Vote')


class Vote(models.Model):
    title = models.CharField(max_length=100, verbose_name="投票标题")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "投票表"


class Options(models.Model):
    opt_title = models.CharField(max_length=100, verbose_name="选项标题")
    opt_poll = models.IntegerField(max_length=3, verbose_name="得票数", default=0)
    opt_vote = models.ForeignKey(Vote, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "选项表"

# class User(AbstractUser):
#     telephone = models.CharField(max_length=11,verbose_name="手机号码")
#     votes = models.ForeignKey(Vote, on_delete=models.CASCADE)
