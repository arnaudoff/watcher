from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from dashboard.sensors.models import Sensor
from dashboard.triggers.models import Trigger

def dashboard_view(request):
    username = None

    if request.user.is_authenticated():	
        username = request.user.username
        sensors = Sensor.objects.filter(user=request.user)
        triggers = Trigger.objects.all()

    context = {
        'username': username,
        'sensors': sensors,
        'triggers': triggers
    }

    return render(request, "dashboard.html", context)
