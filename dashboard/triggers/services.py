from django.core.mail import send_mail

def send_user_intruder_notification(trigger_metadata):
    send_mail(
            'Intruder detected',
            'One of the sensors ({}) of the alarm system detected an intruder at {}.'
            .format(trigger_metadata.sensor.name, trigger_metadata.time_triggered),
            'foo@bar.com',
            ['foo@bar.com'],
            fail_silently=False)
