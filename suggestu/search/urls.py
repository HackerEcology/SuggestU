# app specific urls
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse
from search import views

urlpatterns = patterns('',
                       (r'^$', views.test),
                       #(r'^test/$', views.test),
)
