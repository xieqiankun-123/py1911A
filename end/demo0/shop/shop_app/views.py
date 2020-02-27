from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.core.paginator import Paginator, Page


# Create your views here.


def index(request):
    ads = Ads.objects.all()
    goods = Good.objects.all()[:8]
    return render(request, 'index.html', locals())


def detail(request, good_id):
    try:
        good = Good.objects.get(id=good_id)
        print(good, "++++")
        return render(request, 'detail.html', locals())
    except Exception as e:
        print(e)
        return HttpResponse(e)


def products(request):
    goods = Good.objects.all()
    paginator = Paginator(goods, 8)
    page = paginator.get_page(request.GET.get("pagenum", 1))
    return render(request, 'products.html', locals())


def shop_cart(request):
    return HttpResponse("购物车界面")
