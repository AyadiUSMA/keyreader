from django.contrib import admin
from django.urls import path
from django.conf.urls import include,url
from keystate import views
from rest_framework.urlpatterns import  format_suffix_patterns
from keystate import api 


urlpatterns = [
    # /keystate
    url(r'^$', views.index, name='index'),

    # /keystate/7/
    url(r'^(?P<Key_id>[0-9]+)/$', views.detail, name='detail'),


]