# django specific
from django.core.context_processors import csrf
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
# app specific
import datetime

#from search import es_query
#from users import control
#from open_facebook import OpenFacebook
#from django_facebook.api import get_persistent_graph
#import json
#from urllib import urlopen

def home(request):    
    c = {}
    c.update(csrf(request))
    context = RequestContext(request)
    return render_to_response('index.html', c, context)
    
def profile(request):
    context = RequestContext(request)
    return render_to_response('profile.html', context)

def results(request, page):    
    query = request.GET.get('q', None)
    if bool(query.split()):
        return render_to_response('results.html', 
                                  {'q' : query })
    else:
        return HttpResponseRedirect('/')
