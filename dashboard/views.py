from django.shortcuts import render
from sensors.models import Sensor
from django.contrib.auth.models import User

def dashboard_view(request):
	print(request.user.is_authenticated())
	print(Sensor.objects.all())

	username = None
	test = None
	if request.user.is_authenticated():	
		username = request.user.username
		test = Sensor.objects.filter(user=request.user)

	context = {
		'username': username,
		'sensor_results': test
	}

	return render(request, "dashboard.html", context)