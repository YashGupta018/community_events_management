from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=200)
    organizer = models.CharField(max_length=200)
    organizer_details = models. TextField()
    rsvp_option = models.BooleanField(default=False)
    attendees = models.ManyToManyField(User, blank=True, related_name='attended_events')
    creator = models. ForeignKey(User, on_delete=models. CASCADE, related_name='created_events')