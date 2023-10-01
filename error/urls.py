from django.urls import path
from error.views import *     # * mean's the All function

app_name = 'error'

urlpatterns = [
    path('', Error, name='error')
]