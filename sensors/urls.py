from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.sensor_list),
    url(r'^create/$', views.sensor_create),
    url(r'^(?P<id>\d+)/$', views.sensor_detail),
    url(r'^update/$', views.sensor_update),
    url(r'^delete/$', views.sensor_delete)
]
