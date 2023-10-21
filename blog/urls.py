from django.urls import path
from blog.views import *     # * mean's the All function

app_name = 'blog'

urlpatterns = [
    path('', blog_view, name='index'),
    path('<int:pid>', blog_single, name='single'),
    #path('name/<str:name>/last-name/<str:family_name>/age/<int:age>', test, name='test'),
]