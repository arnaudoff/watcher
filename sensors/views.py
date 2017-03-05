from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from .forms import SensorForm
from .models import Sensor

def sensor_create(request):
    form = SensorForm(request.POST or None)
    if form.is_valid():
        sensor = form.save(commit=False)
        sensor.save()
        return HttpResponseRedirect(sensor.get_absolute_url())

    context = {
        "form": form
    }

    return render(request, "sensors/create.html", context)

def sensor_detail(request, id=None):
    sensor = get_object_or_404(Sensor, id=id)

    context = {
        "sensor": sensor
    }

    return render(request, "sensors/detail.html", context)

def sensor_list(request):
    sensors = Sensor.objects.all()

    context = {
        "sensors": sensors
    }

    return render(request, "sensors/index.html", context)

def sensor_update(request, id=None):
    sensor = get_object_or_404(Post, id=id)

    form = SensorForm(request.POST or None, instance=sensor)
    if form.is_valid():
        sensor = form.save(commit=False)
        sensor.save()
        return HttpResponseRedirect(sensor.get_absolute_url())

    context = {
        "sensor": sensor
        "form": form
    }

    return render(request, "sensors/update.html", context)

def sensor_delete(request):
    return HttpResponse("<h1>Sensors home</h1>")
