from django.core.urlresolvers import reverse
from search import views
from django.conf.urls import patterns
from scrapers import views

urlpatterns = patterns('',
                       (r'^deploy/(?P<spider>[\w.@+-]+)/?$', views.deploy,),
                       (r'^render/(?P<spider>[\w.@+-]+)/(?P<job>[\w.@+-]+)/?$', views.render,),
                       (r'^_spiders', views.list_spiders),
                       (r'^_jobs', views.list_jobs),
                       (r'^test/?$', views.test),

                       (r'^_items/?$', views.list_items, 
                        {'spider' : '',
                         'dump' : ''}),
                       (r'^_items/(?P<spider>[\w.@+-]+)/?$',  views.list_items,
                        {'dump' : ''}),                        
                       (r'(?P<spider>[\w.@+-]+)/(?P<dump>[\w.@+-]+)/?$', 
                        views.list_items,),
                    )
