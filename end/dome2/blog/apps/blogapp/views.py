from django.shortcuts import render, redirect, reverse

# Create your views here.
from django.http import HttpResponse
from .models import *

from django.core.paginator import Paginator, Page
from .forms import *


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
    typepage = request.GET.get("typepage")
    year = request.GET.get("year")
    month = request.GET.get("month")
    category_id = request.GET.get("category_id")
    tag_id = request.GET.get("tag_id")
    if typepage == "date":
        article = Article.objects.filter(create_time__year=year, create_time__month=month)
    elif typepage == "category":
        try:
            category = Category.objects.get(id=category_id)
            article = category.article_set.all()
        except Exception as e:
            print(e)
            return HttpResponse("分类不合法")
    elif typepage == "tag":
        try:
            tag = Tag.objects.get(id=tag_id)
            article = tag.article_set.all()
        except Exception as e:
            print(e)
            return HttpResponse("分类不合法")
    else:
        article = Article.objects.all()
    paginator = Paginator(article, 2)
    page = paginator.get_page(request.GET.get("pagenum", 1))
    return render(request, 'index.html', locals())


def detail(request, article_id):
    if request.method == "GET":
        try:
            cf = CommentForm()
            article = Article.objects.get(id=article_id)
            return render(request, 'single.html', locals())
        except Exception as e:
            print(e)
            return HttpResponse("没有这篇文章")
    elif request.method == "POST":
        try:
            cf = CommentForm(request.POST)
            comment = cf.save(False)
            article = Article.objects.get(id=article_id)
            print(comment, "+++++")
            comment.article = article
            comment.save()
            url = reverse("blogapp:detail", args=(article_id,))
            return redirect(to=url)
        except Exception as e:
            print(e)
            return HttpResponse("没有这篇文章")




def contact(request):
    return render(request, 'contact.html')
    # return HttpResponse("联系我们")
