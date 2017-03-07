from django.contrib import admin
from .models import (Trigger, Capture)

class TriggerModelAdmin(admin.ModelAdmin):
    list_display = ["time_triggered", "__str__"]
    list_filter = ["time_triggered"]

    class Meta:
        model = Trigger

class CaptureModelAdmin(admin.ModelAdmin):
    list_display = ["contents"]

    class Meta:
        model = Capture

admin.site.register(Trigger, TriggerModelAdmin)
