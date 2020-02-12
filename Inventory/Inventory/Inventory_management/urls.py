from django.conf.urls import url

<<<<<<< HEAD
from .views import *

#Urls patters here
urlpatterns = [
    url(r'^$', home, name='home'),

    url(r'^Desktops/$', display_desktops, name='display_desktops'),
    url(r'^Laptops/$', display_laptops, name='display_laptops'),
    url(r'^Mobiles/$', display_mobiles, name='display_mobiles'),

    url(r'^Add-Desktop/$', add_desktops, name='add_desktops'),
    url(r'^Add-Laptop/$', add_laptops, name='add_laptops'),
    url(r'^Add-Mobile/$', add_mobiles, name='add_mobiles'),

    url(r'^Desktops/Edit_Desktop/(?P<pk>\d+)$', edit_desktop, name='edit_desktop'),
    url(r'^Laptops/Edit-Laptop/(?P<pk>\d+)$', edit_laptop, name='edit_laptop'),
    url(r'^Mobiles/Edit-Mobile/(?P<pk>\d+)$', edit_mobiles, name='edit_mobile'),

    url(r'^Desktops/Delete_Desktop/(?P<pk>\d+)$', delete_desktop, name='delete_desktop'),
    url(r'^Laptops/Delete_Laptop/(?P<pk>\d+)$', delete_laptop, name='delete_laptop'),
    url(r'^Mobiles/Delete_Mobile/(?P<pk>\d+)$', delete_mobile, name='delete_mobile'),

=======
from .views import home

#Urls patters here
urlpatterns = [
    url(r'^', home, name='home'),
>>>>>>> master
]