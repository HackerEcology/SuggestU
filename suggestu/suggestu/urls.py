## project wide urls
####################
from django.conf.urls import patterns, include, url
# from django.views.generic.simple import redirect_to
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse
from django.contrib import admin
admin.autodiscover()
import settings
from django.conf import settings

## urls from each app
#####################
import search.urls
import users.urls
import relater.urls
import scrapers.urls
from suggestu import views

# Patterns
urlpatterns = patterns('',
                       # urls specific to this app
                       url(r's_rel', include(relater.urls)),
                       url(r'search/', include(search.urls)),
                       url(r'scrape/', include(scrapers.urls)),
                       # Uncomment the admin/doc line below to enable admin documentation:
                       #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       # catch all, redirect to search home view
                       
                       (r'^facebook/', include('django_facebook.urls')),
                       (r'^accounts/', include('django_facebook.auth_urls')), 
                       
                       (r'^profile/?$', views.profile),
                       (r'^$', views.home),
                       (r'^results/(?P<page>[\w.@+-]+)/?$', views.results,),

                       #url(r'^social-auth/', 'suggestu.app.views.social_auth'),
                       url(r'^login/?$', 'suggestu.app.views.login'),
                       url(r'^signup-email/', 'suggestu.app.views.signup_email'),
                       url(r'^email-sent/', 'suggestu.app.views.validation_sent'),
                       url(r'^logout/$', 'suggestu.app.views.logout'),
                       url(r'^done/$', 'suggestu.app.views.done', name='done'),
                       url(r'^email/$', 'suggestu.app.views.require_email', name='require_email'),
		       url(r'^newsdump/$','suggestu.app.views.newsdump'),
                       url(r'', include('social.apps.django_app.urls', namespace='social')),                    
)

if settings.MODE == 'userena':
    urlpatterns += patterns('',
                            (r'^accounts/', include('userena.urls')),
                        )
elif settings.MODE == 'django_registration':
    urlpatterns += patterns('',
                            (r'^accounts/', include(
                                'registration.backends.default.urls')),
                        )
    
    
if settings.DEBUG:
    urlpatterns += patterns('',
                            url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
                                'document_root': settings.MEDIA_ROOT,
                            }),
    )
