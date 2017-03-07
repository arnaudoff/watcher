from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from .forms import TriggerForm
from .models import Trigger

def trigger_create(request):
    form = TriggerForm(request.POST or None)
    if form.is_valid():
        trigger = form.save(commit=False)
        trigger.save()
        return HttpResponseRedirect(trigger.get_absolute_url())

    context = {
        "form": form
    }

    return render(request, "triggers/create.html", context)

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

def trigger_delete(request):
    return HttpResponse("delete")
