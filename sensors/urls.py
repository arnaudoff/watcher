from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.sensor_list),
    url(r'^create/$', views.sensor_create),
    url(r'^(?P<id>\d+)/$', views.sensor_detail, name='detail'),
    url(r'^(?P<id>\d+)/edit$', views.sensor_update, name='update'),
    url(r'^delete/$', views.sensor_delete)
]
