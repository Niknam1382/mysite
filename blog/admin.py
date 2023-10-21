from django.contrib import admin
from blog.models import Post
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = "-empty-"
    # fields = ("title",)
    list_display = ['title','author','counted_views','status','published_date']
  # list_display = ('counted_views',) it's ok
    list_filter = ('status','author')
    # ordering = ['-created_date']      { i'm using ordering in the Meta Class in Class Post }
    search_fields = ['title','content']
# admin.site.register(Post, PostAdmin)