from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^sign_in', views.show),
    url(r'^register', views.show_reg),
    url(r'^regging', views.register),
    url(r'logging', views.sign_in),
    url(r'^logout', views.logout),
    url(r'^$', views.show),
]