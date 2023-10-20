from django.shortcuts import render, get_object_or_404
from blog.models import Post
import datetime
from django.http import Http404


# Create your views here.

def blog_view(request):
    current_datetime = datetime.datetime.now()
    posts = Post.objects.filter(status=1).exclude(published_date__gt=current_datetime)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)

def blog_single(request, pid):
    post = get_object_or_404(Post, pk=pid)
    context = {'post': post}

    c = Post.objects.get(id = pid)
    c.counted_views = c.counted_views + 1
    c.save()

    return render(request, 'blog/blog-single.html', context)
    


'''
def test(request):
    posts = Post.objects.all()
  # posts = Post.objects.filter(status = 1)
    context = {'name':'Mohammad Mahdi', 'last_name':'Niknam', 'posts': posts}
    return render (request, 'test.html', context)
'''

'''
def test (request, name, family_name, age):
    context = {'name':name, 'family_name':family_name, 'age':age}
    return render(request, 'test.html', context)
'''

'''
def test (request, pid) :
    # post = Post.objects.get(id = pid)
    post = get_object_or_404(Post, pk=pid)
    context = {'post': post}
    return render(request, 'test.html', context)
'''
'''
def counter (func) :
    def wrapper() :
        func()
        c = Post.objects.get(id = pid)
        c.counted_views = c.counted_views - 5
        c.save()
    return wrapper

@counter
'''
def test (request, pid) :
    # post = Post.objects.get(id = pid)
    published_date = Post.objects.get(id = pid).published_date
    published_date = str(published_date)

    now = datetime.datetime.now()
    now = str(now)
    now = now[:19]

    year = int(now[:4])
    month = int(now[5:7])
    day = int(now[8:10])
    hour = int(now[11:13])
    minute = int(now[14:16])
    second = int(now[17:19])

    p_year = int(published_date[:4])
    p_month = int(published_date[5:7])
    p_day = int(published_date[8:10])
    p_hour = int(published_date[11:13])
    p_minute = int(published_date[14:16])
    p_second = int(published_date[17:19])

    x = False
    if year > p_year:
        x = True
    elif year == p_year:
        if month > p_month:
            x = True
        elif month == p_month:
            if day > p_day:
                x = True
            elif day == p_day:
                if hour > p_hour:
                    x = True
                elif hour == p_hour:
                    if minute > p_minute:
                        x = True
                    elif minute == p_minute:
                        if second > p_second:
                            x = True

    c = Post.objects.get(id = pid)

    if x == True :
        post = Post.objects.get(id = pid)
        context = {'post': post}
        c.counted_views = c.counted_views + 1
        c.save()
        return render(request, 'test.html', context)
        
    else :
        raise Http404

'''
# @counter
def test (request, pid) :
    current_datetime = datetime.datetime.now()
    posts = get_object_or_404(Post, pk=pid)
    posts = posts.exclude(published_date__gt=current_datetime)  # exclude errors
   #posts = Post.objects.filter(status=1)
    context = {'post': posts}
    return render(request, 'test.html', context)
'''
