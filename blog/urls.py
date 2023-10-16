from django.urls import path
from blog.views import *     # * mean's the All function

app_name = 'blog'

urlpatterns = [
    path('', blog_view, name='index'),
    path('single', blog_single, name='single'),
    path('test', test, name='test'),
]