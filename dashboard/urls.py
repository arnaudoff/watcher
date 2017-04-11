from django.conf.urls import url

from dashboard.views import (dashboard_view, add_sensor_view)

urlpatterns = [
	url(r'^$', dashboard_view, name='dashboard'),
	url(r'^add_sensor/', add_sensor_view, name='add_sensor')
]