# -*- encoding: utf-8 -*-
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^bar-code/generated/$', views.BarCodeCreateView.as_view(), name='generated'),
    url(r'^bar-code/upload/$', views.upload, name='upload'),
    #url(r'^bar-code/csv/$', views.upload, name='csv'),
    url(r'^bar-code/list/$', views.BarCodeListView.as_view(), name='list'),
    url(r'^bar-code/(?P<slug>[-\w\W\d]+)/$', views.BarCodeDetailView.as_view(), name='detail'),
]