from django import template
from datetime import datetime
from blog.models import Post, Category, Comment

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

@register.inclusion_tag('blog/blog-popular-post.html')
def latestposts(arg=3):
    posts = Post.objects.filter(status=1).order_by('-published_date')[:arg]
    return {'posts':posts}

@register.inclusion_tag('blog/blog-post-categories.html')
def postcategories():
    posts = Post.objects.filter(status=1)
    category = Category.objects.all()
    cat_dict = {}
    for name in category:
        cat_dict[name] = posts.filter(category=name).count()
    return {'categories':cat_dict}

@register.simple_tag(name='comment_count')
def function(pid):
    return Comment.objects.filter(post=pid,approved=True).count()