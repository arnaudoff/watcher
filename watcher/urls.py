from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^users/', include("users.urls")),
    url(r'^dashboard/', include("dashboard.urls")),
    url(r'^api-auth/', include('rest_framework.urls'))
]
