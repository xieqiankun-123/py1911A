from django.conf.urls import url
from django.http import HttpResponse
from . import views

app_name = "booktest"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/111$', views.about, name='about'),
    url(r'^detail/(\d+)/$', views.detail, name='detail'),
    url(r'^deletebook/(\d+)/$', views.deletebook, name='deletebook'),
    url(r'^deletehero/(\d+)$', views.deletehero, name='deletehero'),
    url(r'^addhero/(\d+)$', views.addhero, name='addhero'),
    url(r'^addbook/$', views.addbook, name='addbook'),
    url(r'^edithero/(\d+)/$', views.edithero, name='edithero'),
    url(r'^editbook/(\d+)/$', views.editbook, name='editbook')
    # url('')

]
