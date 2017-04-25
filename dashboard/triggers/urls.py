from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from dashboard.triggers import views

router = DefaultRouter()
router.register(r'triggers', views.TriggerViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^(?P<id>\d+)/$', views.trigger_detail, name='detail')
]
