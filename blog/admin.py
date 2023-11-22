from django.contrib import admin
from blog.models import Post, Category, Comment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = "-empty-"
    # fields = ("title",)
    list_display = ['title','author','counted_views','status','published_date']
    # list_display = ('counted_views',) it's ok
    list_filter = ('status','author')
    # ordering = ['-created_date']      { i'm using ordering in the Meta Class in Class Post }
    search_fields = ['title','content']

    summernote_fields = ('content',)

class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = "-empty-"
    list_display = ['name','post','approved','created_date']
    list_filter = ('post','approved')
    search_fields = ['name','post']

admin.site.register(Comment, CommentAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Category)