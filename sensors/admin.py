from django.contrib import admin

from .models import (Sensor, Trigger, Capture)

class SensorModelAdmin(admin.ModelAdmin):
    list_display = ["name", "timestamp"]
    list_filter = ["timestamp"]
    search_fields = ["name"]

    class Meta:
        model = Sensor

class TriggerModelAdmin(admin.ModelAdmin):
    list_display = ["time_triggered"]
    list_filter = ["time_triggered"]

    class Meta:
        model = Trigger

# TODO: Display the contents in the template properly
class CaptureModelAdmin(admin.ModelAdmin):
    list_display = ["contents"]

    class Meta:
        model = Capture

admin.site.register(Sensor, SensorModelAdmin)
admin.site.register(Trigger, TriggerModelAdmin)
admin.site.register(Capture, CaptureModelAdmin)
