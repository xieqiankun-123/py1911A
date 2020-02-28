"""drf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from shop.views import *
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from .settings import MEDIA_ROOT
from django.conf.urls import url
from django.views.static import serve
from shop.views import *

router = routers.DefaultRouter()
router.register("categorys", CategoryViewSets)
# router.register("goods", GoodViewSets)
# router.register("goodimgs", GoodImagesViewSets)

urlpatterns = [
    path('admin/', admin.site.urls),
    url('media/(?P<path>.*)', serve, {'document_root': MEDIA_ROOT}),
    url(r'^categorylist/$', category_list, name="category_list"),
    url(r'^categorydetail/(\d+)/$', category_detail, name="category_detail"),
    url(r'^goodlist/$', good_list, name="good_list"),
    url(r'^gooddetail/(\d+)/$', good_detail, name="good_detail"),

    path('api/v1/docs/', include_docs_urls(title="RestFulAPI", description="RestFulAPI|v1")),
    path('api/v1/', include(router.urls)),
    path('', include('rest_framework.urls')),
]
