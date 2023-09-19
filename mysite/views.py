from django.http import HttpResponse, JsonResponse

def http_test(request) :
    return HttpResponse ('<h1>Hello Django! This is the first http-test</h1>')

def json_test(request) :
    return JsonResponse ({'name' : 'Mohammad mahdi'})

# this is just my test
def my_test(request) :
    return HttpResponse('./my test/index.html') # I have a little problem :)