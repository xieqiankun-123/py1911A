from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from .models import *
from django.core.paginator import Paginator, Page
from .forms import CommentForm


# Create your views here.


def index(request):
    type_page = request.GET.get("type_page")
    year = None
    month = None
    category_id = None
    tag_id = None
    if type_page == "date":
        year = request.GET.get("year")
        month = request.GET.get("month")
        articles = Article.objects.filter(create_time__year=year, create_time__month=month)
    elif type_page == "category":
        try:
            category_id = request.GET.get("category_id")
            category = Category.objects.get(id=category_id)
            articles = category.article_set.all()
        except Exception as e:
            print(e)
            return HttpResponse("分类不合法")
    elif type_page == "tag":
        try:
            tag_id = request.GET.get("tag_id")
            tag = Tag.objects.get(id=tag_id)
            articles = tag.article_set.all()
        except Exception as e:
            print(e)
            return HttpResponse("标签不合法")
    else:
        articles = Article.objects.all()
    paginator = Paginator(articles, 2)
    page = paginator.get_page(request.GET.get("pagenum", 1))
    ads = Ads.objects.all()
    return render(request, 'index.html', locals())


def detail(request, article_id):
    if request.method == "GET":
        try:
            cf = CommentForm()
            article = Article.objects.get(id=article_id)
            return render(request, 'single.html', locals())
        except:
            return HttpResponse("文章不存在")
    elif request.method == "POST":
        try:
            article = Article.objects.get(id=article_id)
            cf = CommentForm(request.POST)
            comment = cf.save(False)
            print(comment)
            comment.article = article
            comment.save()
            url = reverse("blog_app:detail",args=(article_id,))
            return redirect(to=url)
        except:
            return HttpResponse("文章不存在")


def contact(request):
    return render(request, 'contact.html')
    # return HttpResponse("联系我们")
