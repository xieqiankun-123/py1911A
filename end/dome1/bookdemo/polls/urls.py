from django.conf.urls import url
from django.http import HttpResponse
from . import views

app_name = "polls"
urlpatterns = [
    url(r'^$', views.index, name='polls_index'),
    url(r'^detail/(\d+)/$', views.detail, name='polls_detail'),
    url(r'^add_option/(\d+)/$', views.add_option, name='polls_add_option'),
    url(r'^add_vote/$', views.add_vote, name='polls_add_vote'),
    url(r'^delete_option/(\d+)/$', views.delete_option, name='polls_delete_option'),
    url(r'^delete_vote/$', views.delete_vote, name='polls_delete_vote'),
]
