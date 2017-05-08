import django
from django.conf import settings
from django.core.mail import send_mail

def send_user_intruder_notification(trigger_metadata):
    send_mail(
            'Intruder detected',
            'One of the sensors ({}) of the alarm system detected an intruder at {}.'
            .format(trigger_metadata.sensor.name, trigger_metadata.time_triggered),
            settings.EMAIL_HOST_USER,
            [settings.EMAIL_HOST_USER],
            fail_silently=False)
