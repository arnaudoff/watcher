from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404

from dashboard.sensors.forms import SensorForm
from dashboard.sensors.models import Sensor

def sensor_create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404

    form = SensorForm(request.POST or None)
    if form.is_valid():
        sensor = form.save(commit=False)
        sensor.user = request.user
        sensor.save()

        messages.success(request, "Successfully created!")
        return HttpResponseRedirect(sensor.get_absolute_url())
    else:
        messages.error(request, "Not successfully created!")

    context = {
        "form": form
    }

    return render(request, "sensors/create.html", context)

def sensor_detail(request, id=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404

    sensor = get_object_or_404(Sensor, id=id)

    context = {
        "sensor": sensor
    }

    return render(request, "sensors/detail.html", context)

def sensor_list(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404

    sensors = Sensor.objects.all()

    context = {
        "sensors": sensors
    }

    return render(request, "sensors/index.html", context)

def sensor_update(request, id=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404

    sensor = get_object_or_404(Post, id=id)

    form = SensorForm(request.POST or None, instance=sensor)
    if form.is_valid():
        sensor = form.save(commit=False)
        sensor.save()
        messages.success(request, "Successfully updated!")
        return HttpResponseRedirect(sensor.get_absolute_url())
    else:
        messages.error(request, "Not successfully updated!")

    context = {
        "sensor": sensor,
        "form": form
    }

    return render(request, "sensors/update.html", context)

def sensor_delete(request, id=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404

    sensor = get_object_or_404(Post, id=id)
    sensor.delete()
    messages.success(request, "Successfully deleted!")
    return redirect("sensors:list")
