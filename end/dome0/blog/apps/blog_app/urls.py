from django.conf.urls import url
from .feed import ArticleFeed
from . import views
from .feed import *

app_name = "blog_app"

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^detail/(\d+)/$', views.detail, name="detail"),
    url(r'^contact/$', views.contact, name="contact"),
    url('rss/', ArticleFeed(), name="rss")
]
