from django.conf.urls import url, include

from dashboard.views import dashboard_view

urlpatterns = [
    url(r'^$', dashboard_view, name='dashboard'),
    url(r'^sensors/', include("dashboard.sensors.urls")),
    url(r'^triggers/', include("dashboard.triggers.urls"))
]
