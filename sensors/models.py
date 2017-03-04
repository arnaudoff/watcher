from django.db import models

class Sensor(models.Model):
    name = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name

class Trigger(models.Model):
    time_triggered = models.DateTimeField()
    sensor = models.ForeignKey('Sensor')

    def __str__(self):
        return "%s %s" % (self.sensor.name, str(self.time_triggered))

class Capture(models.Model):
    contents = models.CharField(max_length=65536)
    trigger = models.ForeignKey('Trigger')
