from django import template
from datetime import datetime
from blog.models import Post

register = template.Library()

@register.simple_tag
def function():
    now = datetime.now()
    time_str = now.strftime("%H:%M:%S")
    return(time_str)

@register.simple_tag(name='total_post')
def function():
    posts = Post.objects.filter(status = 1).count()
    return posts

@register.simple_tag(name='posts')
def function():
    posts = Post.objects.filter(status = 1)
    return posts
