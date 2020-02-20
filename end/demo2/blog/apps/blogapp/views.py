from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from .models import *

from django.core.paginator import Paginator, Page


# 一个Page中有  object_list代表当前页的所有对象
# has_next 是不是有下一页
# has_previous 是否有上一页
# next_page_number 下一页的编号
# previous_page_number 上一页的编号
# self.number 当前页的编号
# self.paginator 当前页的分页器

# 一个Paginator中的object_list 代表所有未分页对象
# self.per_page 每一页有几个对象
# get_page(self, number): 从分页器中取第几页
# page_range(self): 返回分页列表
def favicon(request):
    return redirect(to="/static/favicon.ico")


def index(request):
    ads = Ads.objects.all()
    article = Article.objects.all()
    paginator = Paginator(article, 2)
    page = paginator.get_page(request.GET.get("pagenum", 1))
    return render(request, 'index.html', {"ads": ads, "page": page})


def detail(request, article_id):
    try:
        article = Article.objects.get(id=article_id)
        return render(request, 'single.html', locals())
    except Exception as e:
        print(e)
        return HttpResponse("没有这篇文章")


def contact(request):
    return render(request, 'contact.html')
    # return HttpResponse("联系我们")
