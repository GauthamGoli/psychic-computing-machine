from django.conf.urls import patterns, url
from clientportal import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'))