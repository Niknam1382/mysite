from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager

# Create your models here.

class Category(models.Model) :
    name = models.CharField(max_length=255)

    def __str__(self) :
        return self.name
    
class Post(models.Model) :
    image = models.ImageField(upload_to='blog/', default='blog/default.jpg')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) # on_delete=models.CASCADE
    title = models.CharField(max_length=255)
    content = models.TextField()
    tags = TaggableManager()
    category = models.ManyToManyField(Category)
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
    
    # def snippets (self) :
    #     return self.content[:150] + ' ...'
    def snippets (self) :
        l = self.content.split()
        l = l[:35]
        return ' '.join(l) + ' ...'
    
    def get_absolute_url(self) :
        return reverse('blog:single', kwargs={'pid':self.id})