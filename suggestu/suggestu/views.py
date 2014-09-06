# django specific
from django.core.context_processors import csrf
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
# app specific
import datetime
import urllib
import requests
#from search import es_query
from users import control
#from open_facebook import OpenFacebook
#from django_facebook.api import get_persistent_graph
import json
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
    results = json.loads(requests.get('http://localhost:9200/qrator/_search?q=' + query).content)
    data = []
    for i in xrange(len(results['hits']['hits'])):
        temp = {}
        temp['type'] = results['hits']['hits'][i]['_type']
        temp['source'] = results['hits']['hits'][i]['_source']
        data.append(temp)

    if bool(query.split()):
        history = control.add_to_history(query, str(request.user))
        if len(history) > 5:
            history = history[-5:]
        return render_to_response('results.html', 
                                  {'q' : query,
                                   'history' : history,
                                   'data': data,
                                   'hits' : results['hits']['total']})
    else:
        return HttpResponseRedirect('/')

'''
def newsdump(request,page):
    news = urllib.request.urlopen("http://http://localhost:6800/items/default/HBR/601f1cf3fc7911e3a9aa14109fdb5de1.jl").read()
    print news
    return
'''
