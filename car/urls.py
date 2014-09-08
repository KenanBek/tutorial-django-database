from django.conf.urls import patterns, url

from car import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^new/$', views.car, name='new'),
    url(r'^modify/$', views.car, name='modify'),
    url(r'^modify/(?P<car_id>[0-9]+)$', views.car, name='modify'),
)
