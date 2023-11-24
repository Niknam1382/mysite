from django.shortcuts import render, get_object_or_404
from blog.models import Post, Comment
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from blog.forms import CommentForm
from django.contrib import messages

# Create your views here.

def blog_view(request, **kwargs):
    now = timezone.now()
    posts = Post.objects.filter(status=1).exclude(published_date__gt=now)
    if kwargs.get('cat_name') is not None:
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username=kwargs['author_username'])
    if kwargs.get('tag_name') :
        posts = posts.filter(tags__name__in=[kwargs['tag_name']])

    posts = Paginator(posts, 4)
    try :
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger :
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)
        
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)

def blog_single(request, pid):

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS, 'Your comment submited successfully')
        else:
            messages.add_message(request,messages.ERROR, 'Your comment didnt submited')

    now = timezone.now()
    posts = Post.objects.filter(status=1).exclude(published_date__gt=now)
    # posts = Post.objects.filter(status=1, published_date__lte=timezone.now()) that's ok too!
    post = get_object_or_404(posts, pk=pid)
    Comments = Comment.objects.filter(post=post.id, approved=True)  #.order_by('-created_date')
    post.counted_views += 1
    post.save()
    
    prev = Post.objects.filter(status=1, published_date__lt=post.published_date).exclude(pk=post.pk).order_by('-published_date').first()
    next = Post.objects.filter(status=1, published_date__gt=post.published_date).exclude(pk=post.pk).order_by('published_date').first()

    form = CommentForm()

    context = {'post': post, 'prev': prev, 'next': next, 'Comments':Comments, 'form': form}
    return render(request, 'blog/blog-single.html', context)

def test(request) :
    return render(request, 'test.html')
'''
def blog_category(request, cat_name):
    posts = Post.objects.filter(status=1)
    posts = posts.filter(category__name=cat_name)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)
'''
def blog_search(request):
    # print(request.__dict__)
    now = timezone.now()
    posts = Post.objects.filter(status=1).exclude(published_date__gt=now)
    if request.method == 'GET':
        # print(request.GET.get('s'))
        if s:= request.GET.get('s'):
            posts = posts.filter(content__contains=s)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)