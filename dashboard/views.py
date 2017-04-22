from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from dashboard.sensors.models import Sensor

def dashboard_view(request):
    username = None
    test = None
    if request.user.is_authenticated():	
        username = request.user.username
        sensor_results = Sensor.objects.filter(user=request.user)

    context = {
        'username': username,
        'sensor_results': sensor_results
    }

    return render(request, "dashboard.html", context)
