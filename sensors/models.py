from django.db import models
from django.core.urlresolvers import reverse

class Sensor(models.Model):
    name = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("detail", kwargs={"id": self.id})
