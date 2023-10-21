from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.utils import timezone

# Create your views here.

def blog_view(request):
    now = timezone.now()
    posts = Post.objects.filter(status=1).exclude(published_date__gt=now)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)

def blog_single(request, pid):
    now = timezone.now()
    posts = Post.objects.filter(status=1).exclude(published_date__gt=now)
    post = get_object_or_404(posts, pk=pid)
    context = {'post': post}
    c = Post.objects.get(id = pid)
    c.counted_views = c.counted_views + 1
    c.save()
    return render(request, 'blog/blog-single.html', context)