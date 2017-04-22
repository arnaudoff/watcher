from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework import viewsets

from dashboard.triggers.models import Trigger
from dashboard.triggers.forms import TriggerForm
from dashboard.triggers.serializers import TriggerSerializer
from dashboard.triggers.services import send_user_intruder_notification

def trigger_detail(request, id=None):
    trigger = get_object_or_404(Trigger, id=id)

    context = {
        "trigger": trigger
    }

    return render(request, "triggers/detail.html", context)

def trigger_list(request):
    triggers = Trigger.objects.all()

    context = {
        "triggers": triggers
    }

    return render(request, "triggers/index.html", context)

class TriggerViewSet(viewsets.ModelViewSet):
    queryset = Trigger.objects.all()
    serializer_class = TriggerSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        send_user_intruder_notification(trigger_metadata=instance)
