from django.shortcuts import render
from sensors.models import Sensor

def dashboard_view(request):
	print(request.user.is_authenticated())
	print(Sensor.objects.all())

	username = None
	if request.user.is_authenticated():	
		username = request.user.username
	context = {
		"username": username
	}

	return render(request, "dashboard.html", context)