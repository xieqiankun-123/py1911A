from django.template import Library
from ..models import GoodCategory

register = Library()


@register.simple_tag
def get_categorys(num=9):
    return GoodCategory.objects.all()[:num]
