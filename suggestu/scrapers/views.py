from django.template import RequestContext
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.http import Http404, HttpResponse, HttpResponseRedirect
import json
from urllib import urlopen
from subprocess import call

def test(request):
    c = {}
    return render_to_response('test.html', c)

def list_spiders(request):
    response = urlopen("http://127.0.0.1:6800/listspiders.json?project=default")
    response = json.loads(response.read())
    return HttpResponse('\n'.join(response['spiders']), content_type="application/json")

def list_jobs(request):
    response = urlopen("http://localhost:6800/listjobs.json?project=default")    
    #response = json.loads(response.read())
    return HttpResponse(response.read(), content_type="application/json")

def deploy(request, spider):
    url = "curl http://localhost:6800/schedule.json -d project=default -d spider=%s" % (spider)
    try:
        call(url.split())
        return HttpResponse("Done!")
    except:
        return HttpResponse("Failed!")

def render(request, spider, job):
    url = "http://127.0.0.1:6800/items/default/%s/%s.jl" % (spider, job)
    response = urlopen(url).read()
    if "404 - No Such Resource" in response:
        return HttpResponse(response)
    else:
        return HttpResponse(json.dumps(response), content_type="application/json")

