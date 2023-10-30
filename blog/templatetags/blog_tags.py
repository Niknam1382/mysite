from django import template
from datetime import datetime
from blog.models import Post

register = template.Library()

@register.simple_tag
def function():
    now = datetime.now()
    time_str = now.strftime("%H:%M")
    return(time_str)

@register.simple_tag(name='total_post')
def function():
    posts = Post.objects.filter(status = 1).count()
    return posts

@register.simple_tag(name='posts')
def function():
    posts = Post.objects.filter(status = 1)
    return posts

@register.filter
def snippet(value, arg= 20):
    return value[:arg] + '...'

@register.inclusion_tag('blog/blog-popular-posts.html')
def latestposts():
    posts = Post.objects.filter(status=1).order_by('-published_date')[:3]
    return {'posts':posts}