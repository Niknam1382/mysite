from django.shortcuts import render

# Create your views here.
import datetime
from django.http import HttpResponse

def time(request) :
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def index_view(request) :
    return HttpResponse ('<h1>Home page</h1>')

def about_view(request) :
    return HttpResponse ('<h1>about us:</h1>')

def contact_view(request) :
    return HttpResponse ('<h1>Contact</h1>')