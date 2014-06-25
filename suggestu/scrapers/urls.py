from django.core.urlresolvers import reverse
from search import views
from django.conf.urls import patterns
from scrapers import views

urlpatterns = patterns('',
                       (r'^deploy/(?P<spider>[\w.@+-]+)/?$', views.deploy,),
                       (r'^render/(?P<spider>[\w.@+-]+)/(?P<job>[\w.@+-]+)/?$', views.render,),
                       (r'^_all', views.list_spiders),
                       (r'^_jobs', views.list_jobs),
                       (r'^test/?$', views.test),
)
