from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.trigger_list),
    url(r'^create/$', views.trigger_create),
    url(r'^(?P<id>\d+)/$', views.trigger_detail, name='detail'),
    url(r'^delete/$', views.trigger_delete)
]
