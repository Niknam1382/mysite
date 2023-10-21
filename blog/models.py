from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model) :
    # image
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    # tag
    # category
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True) #(خودمون تعریفش میکنیم کی پابلیش بشه)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    class Meta :
        # ordering = ['-created_date']          # i chenged the ordering for my exercise in 6th django chapter
        ordering = ['-published_date']

# SELECT * FROM Post
# SELECT * FROM Post WHERE status = 1
    def __str__ (self) :
        return '{} - {}'.format(self.title, self.id)
    
    