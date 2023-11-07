from django.shortcuts import render
import datetime
from django.http import HttpResponse, JsonResponse
from website.models import contact
# Create your views here.


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

def test_view(request) :
    if request.method == "POST":
        # print('post')     YES
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        c = contact()
        c.name = name
        c.email = email
        c.subject = subject
        c.message = message
        c.save()
    return render(request, 'website/test.html',{})