from django.shortcuts import render

# Create your views here.

def Error(request) :
    return render (request, '404/index.html')
