from django import forms
from rmnd.models import Event

class NewEventForm(forms.ModelForm):
    # date = forms.DateField(input_formats=('%m/%d/%Y',))

    class Meta:
        model = Event
