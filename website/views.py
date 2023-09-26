from django.shortcuts import render

# Create your views here.
import datetime
from django.http import HttpResponse, JsonResponse

def http_test(request) :
    return HttpResponse ('<h1>Hello Django! This is the first http-test</h1>')

def json_test(request) :
    return JsonResponse ({'name' : 'Mohammad mahdi'})

def time(request) :
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def index_view(request) :
    return render(request, 'website/index.html')

def about_view(request) :
    return render(request, 'website/about.html')

# def contact_view(request) :
#     return HttpResponse ('<h1>Contact</h1>')

def contact_view(request) :
    return render(request, 'website/contact.html')