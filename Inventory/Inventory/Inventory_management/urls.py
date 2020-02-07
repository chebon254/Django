from django.conf.urls import url

from .views import home

#Urls patters here
urlpatterns = [
    url(r'^', home, name='home'),
]