from django.conf.urls import url

from .views import *


#Url patterns here
urlpatterns = [
    url(r'^', home_view, name='home'),
]