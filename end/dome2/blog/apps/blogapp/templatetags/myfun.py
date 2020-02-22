from django.template import Library
from ..models import Article, Category, Tag

register = Library()


@register.filter
def dateFormat(data):
    return "%d-%d-%d" % (data.year, data.month, data.day)


@register.filter
def authorFormat(author, info):
    return info + author


@register.simple_tag
def get_article_list(num=3):
    return Article.objects.all().order_by("-create_time")[:num]


@register.simple_tag
def get_dates_list(num=3):
    dates = Article.objects.dates("create_time", "month")[:num]
    return dates


@register.simple_tag
def get_category_list(num=3):
    return Category.objects.all()[:num]


@register.simple_tag
def get_tags():
    return Tag.objects.all()
