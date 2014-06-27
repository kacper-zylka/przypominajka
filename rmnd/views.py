from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from rmnd.models import Event
from rmnd.forms import NewEventForm

def index(request):
    context = {}
    return render(request, 'rmnd/index.html', context)

class EventList(ListView):
    model = Event
    template_name = "rmnd/list.html"

def new_event(request):
    if request.method == 'POST':
        form = NewEventForm(request.POST)
        if form.is_valid():
            event = Event()
            event.name = request.POST['name']
            event.date = request.POST['date']
            event.description = request.POST['description']
            event.save()

            return redirect('event_list')
    else:
        form = NewEventForm()

    return render(request, 'rmnd/new_event.html', {'form' : form})

class EventDetail(DetailView):
    model = Event
    template_name = 'rmnd/event.html'
























