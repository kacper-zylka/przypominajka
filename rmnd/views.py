from django.shortcuts import render, get_object_or_404
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

    def get_context_data(self, **kwargs):
        context = super(EventList, self).get_context_data(**kwargs)
        context['event_list'] = Event.objects.all()
        return context

def new_event(request):
    if request.method == 'POST':
        form = NewEventForm(request.POST)
        if form.is_valid():
            event = Event()
            event.name = request.POST['name']
            event.date = request.POST['date']
            event.description = request.POST['description']
            event.save()

            return HttpResponseRedirect('events')
    else:
        form = NewEventForm()

    return render(request, 'rmnd/new_event.html', {'form' : form})

def event_detail(request, event_id):


    return HttpResponse(event_id)

class EventDetail(DetailView):
    model = Event
    # slug =
    template_name = 'rmnd/event.html'
    # context_object_name

    def get_context_data(self, **kwargs):
        context = super(EventDetail, self).get_context_data(**kwargs)
        context['event'] = get_object_or_404(Event, pk=event_id)
        return context