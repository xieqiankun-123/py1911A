from django.template import Library
from ..models import Article, Category, Tag

register = Library()


@register.simple_tag
def get_article_list(num=3):
    return Article.objects.all().order_by("-create_time")[:num]


@register.simple_tag
def get_tag_list():
    return Tag.objects.all()


@register.simple_tag
def get_category_list(num=3):
    return Category.objects.all()[:num]


@register.simple_tag
def get_article_dates(num=3):
    return Article.objects.dates("create_time", "month")[:num]
