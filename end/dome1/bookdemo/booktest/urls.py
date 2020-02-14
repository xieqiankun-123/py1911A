from django.conf.urls import url
from django.http import HttpResponse
from . import views

app_name = "booktest"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'detail/(\d+)/', views.detail, name='detail')

]
