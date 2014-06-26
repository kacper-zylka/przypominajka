from django.db import models

# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    date = models.DateField()

    def __unicode__(self):
        return self.name
