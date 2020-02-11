from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=20)
    bpub_date = models.DateField(default="1983-06-01")


class Hero(models.Model):
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=5, choices=(("meal", "男"), ("female", "女")))
    content = models.CharField(max_length=100)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
