from django.db import models

# Create your models here.
class Post(models.Model) :
    # image
    # author
    title = models.CharField(max_length=255)
    content = models.TextField()
    # tag
    # category
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True) #(خودمون تعریفش میکنیم کی پابلیش بشه)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
# SELECT * FROM Post
# SELECT * FROM Post WHERE status = 1
    def __str__ (self) :
        return '{} - {}'.format(self.title, self.id)