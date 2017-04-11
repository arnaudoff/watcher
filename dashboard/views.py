from django.shortcuts import render, redirect
from sensors.models import Sensor
from django.contrib.auth.models import User

from .forms import AddSensorForm

def dashboard_view(request):
	print(request.user.is_authenticated())
	print(Sensor.objects.all())

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

def add_sensor_view(request):
	print(request.user.is_authenticated())
	title = "Add sensor"

	form = AddSensorForm(request.POST or None)
	if form.is_valid():
		sensor = form.save(commit=False)
		name = form.cleaned_data.get("name")
		active = form.cleaned_data.get("active")
		sensor = Sensor.objects.create(name=name, user=request.user, active=active)

		return redirect('/dashboard/')

	context = {
		'form': form,
		'title': title
	}

	return render(request, "add_sensor.html", context)