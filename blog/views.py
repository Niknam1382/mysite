from django.shortcuts import render, get_object_or_404
from blog.models import Post
import datetime


# Create your views here.
def blog_view(request):
    posts = Post.objects.filter(status = 1)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)

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

def blog_single(request):
    context={'title':'Bitcoin Crashed', 'content':'Bitcoin uses peer-to-peer technology to operate with no central authority or banks; managing transactions and the issuing of bitcoins is carried out collectively by the network. Bitcoin is open-source; its design is public, nobody owns or controls Bitcoin and everyone can take part. Through many of its unique properties, Bitcoin allows exciting uses that could not be covered by any previous payment system.', 'author':'Mohammad Mahdi Niknam'}
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
    
    if x == True :
        # post = get_object_or_404(Post, pk=pid)
        post = Post.objects.get(id = pid)
        context = {'post': post}
        return render(request, 'test.html', context)
    else :
        obj = get_object_or_404(Post, pk=pid)
        return render (request)
    