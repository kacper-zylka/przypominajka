from django.db import models

# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    description = models.TextField(max_length=200)

    def __unicode__(self):
        return self.name
