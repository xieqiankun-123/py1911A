from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=20)
    price = models.FloatField(default=0)
    bpub_date = models.DateField(default="1983-06-01")
    def __str__(self):
        return self.title


class Hero(models.Model):
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=6, choices=(('male', '男'), ('female', "女")), default='male')
    content = models.CharField(max_length=100)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
