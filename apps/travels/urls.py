from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^add/$', views.add),
    url(r'^adding/$', views.adding),
    url(r'^destination/(?P<name>\d+)/', views.destination),
    url(r'^join/(?P<name>\d+)/', views.join),
    url(r'^$', views.dashboard),
]