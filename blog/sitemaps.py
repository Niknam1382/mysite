from django.contrib.sitemaps import Sitemap
# from django.db.models.base import Model
from blog.models import Post


class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Post.objects.filter(Status=True)
        # return Post.objects.all()

    def lastmod(self, obj):
        return obj.published_date
    
    '''def location(self, obj: Model) -> str:
        return super().location(obj)'''