from django.contrib import admin
from django.conf.urls import url
from . import views

app_name = "shop_app"

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^detail/(\d+)/$', views.detail, name="detail"),
    url(r'products/', views.products, name='products'),
    url(r'^shop_cart/$', views.shop_cart, name='shop_cart')
]
