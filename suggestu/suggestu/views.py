# django specific
from django.core.context_processors import csrf
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
# app specific
import datetime

#from search import es_query
from users import control
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
    ## Optionally, include autocomplete
    # http://suggestqueries.google.com/complete/search?client=chrome&q=how+to <-- return JSON based txt file
    # OR http://google.com/complete/search?q=how+to&output=toolbar <-- Returns XML with just the suggestions.
    query = request.GET.get('q', None)
    if bool(query.split()):
        history = control.add_to_history(query, str(request.user))
        if len(history) > 5:
            history = history[-5:]
        return render_to_response('results.html', 
                                  {'q' : query,
                                   'history' : history})
    else:
        return HttpResponseRedirect('/')
