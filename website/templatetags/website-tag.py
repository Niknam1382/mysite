from django import template
from blog.models import Post, Category

register = template.Library()

@register.inclusion_tag('website/last-post.html')
def lastpost(arg=6):
    posts = Post.objects.filter(status=1).order_by('-published_date')[:arg]
    return {'posts':posts}
    '''
    posts = Post.objects.filter(status=1)
    category = Category.objects.all()
    cat_dict = {}
    for name in category:
        cat_dict[name] = posts.filter(category=name).count()
    return {'categories':cat_dict}
    '''