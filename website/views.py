from django.shortcuts import render
import datetime
from django.http import HttpResponse, JsonResponse ,HttpResponseRedirect
from website.models import contact
from website.forms import NameForm, ContactForm , NewsletterForm
from django.contrib import messages
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
    if request.method == 'POST' :
        form = ContactForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.name = 'Anonymous'
            obj.save()
            messages.add_message(request,messages.SUCCESS, 'Your ticket submited successfully')
        else :
            messages.add_message(request,messages.ERROR, 'Your ticket didnt submited')
    form = ContactForm()
    return render(request, 'website/contact.html', {'form':form})

def test_view(request) :
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # name = form.cleaned_data['name'] # for NameForm
            form.save()
            return HttpResponse('<h1>Done</h1>')
        else:
            return HttpResponse('Not_Valid') # if name on form is incorrect

    form = ContactForm()
    return render(request, 'website/test.html',{'form': form})

def newsletter_view(request) :
    if request.method == "POST" :
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')