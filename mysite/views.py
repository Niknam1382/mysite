# from django.http import HttpResponse
from django.shortcuts import render
def timer_view(request):
    # return HttpResponse('test')
    return render (request,'landing.html')