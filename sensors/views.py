from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Sensor

def sensor_create(request):
    return HttpResponse("<h1>Sensors home</h1>")

def sensor_detail(request, id=None):
    sensor = get_object_or_404(Sensor, id=id)

    context = {
        "sensor": sensor
    }

    return render(request, "detail.html", context)

def sensor_list(request):
    sensors = Sensor.objects.all()

    context = {
        "sensors": sensors
    }

    return render(request, "index.html", context)

def sensor_update(request):
    return HttpResponse("<h1>Sensors home</h1>")

def sensor_delete(request):
    return HttpResponse("<h1>Sensors home</h1>")
