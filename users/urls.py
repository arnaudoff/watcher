from django.conf.urls import url

from users.views import (login_view)

urlpatterns = [
	url(r'^login/', login_view, name='login')
]