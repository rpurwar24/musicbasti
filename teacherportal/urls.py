from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^$', index,name='teacher_home'),
    url(r'^logout/$', logout,name='teacher_logout'),
]