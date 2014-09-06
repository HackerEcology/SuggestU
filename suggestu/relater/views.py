from django.template import RequestContext
from django.core.context_processors import csrf
from django.shortcuts import render_to_response, render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from urllib import urlopen 

def relate(request):    
    s1 = request.GET.get('s1', None)
    s2 = request.GET.get('s2', None)
    #c = {}
    #return render_to_response('test.html', c)
    resp = '<b>Welcome to Sentence relater API</b>'
    resp += '<ul>'
    resp += '<li>'+str(s1)+'</li>'
    resp += '<li>'+str(s2)+'</li>'
    resp += '</ul>'
    return HttpResponse(resp)

def srelate(request):
    s1 = request.GET.get('s1', None)
    s2 = request.GET.get('s2', None)
    url = "http://127.0.0.1:5000/" + s1 + "/" + s2
    resp = urlopen(url)
    return HttpResponse(float(resp.read()))

# def srelate(request):
#     s = dir(request)
#     resp = ''
#     for i in s:
#         resp += i + '<br/>'
#     return HttpResponse(resp)
