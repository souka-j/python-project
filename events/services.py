# services.py
from django.utils import timezone

def is_event_in_future(event):
    
    return event.date > timezone.now()

def is_capacity_valid(capacity):
   
    return capacity > 0
