from django import forms
from rmnd.models import Event

class NewEventForm(forms.ModelForm):
    class Meta:
        model = Event