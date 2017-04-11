from django.contrib import admin

from .models import Sensor

class SensorModelAdmin(admin.ModelAdmin):
    list_display = ["name", "timestamp", "user", "active"]
    list_filter = ["timestamp"]
    search_fields = ["name"]

    class Meta:
        model = Sensor

admin.site.register(Sensor, SensorModelAdmin)
