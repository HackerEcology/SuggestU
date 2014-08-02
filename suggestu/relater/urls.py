# app specific urls
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse
from relater import views

urlpatterns = patterns('',
                       url(r'$', views.relate),
                   )
