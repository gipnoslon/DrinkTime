from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^(?P<name>[a-zA-Zа-яА-Я -_]{3,})_(?P<pk>\d+)$', views.buhlo_detail),
    url(r'^search/$', views.choicekey),
    url(r'^searchname/$', views.choicename),
] 
