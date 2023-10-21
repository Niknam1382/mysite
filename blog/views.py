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
    # posts = Post.objects.filter(status=1, published_date__lte=timezone.now()) that's ok too!
    post = get_object_or_404(posts, pk=pid)
    post.counted_views += 1
    post.save()
    context = {'post': post}

    return render(request, 'blog/blog-single.html', context)