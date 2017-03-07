from django.core.urlresolvers import reverse
from django.db import models

from sensors.models import Sensor

class Trigger(models.Model):
    time_triggered = models.DateTimeField()
    sensor = models.ForeignKey(Sensor)

    def __str__(self):
        return "%s %s" % (self.sensor.name, str(self.time_triggered))

    def get_absolute_url(self):
        return reverse("detail", kwargs={"id": self.id})

class Capture(models.Model):
    contents = models.CharField(max_length=65536)
    trigger = models.ForeignKey(Trigger)

    def __str__(self):
        return self.contents

    def get_absolute_url(self):
        return reverse("detail", kwargs={"id": self.id})

