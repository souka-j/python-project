# services.py
from django.utils import timezone

def is_event_in_future(event):
    """Vérifie si l’événement est dans le futur"""
    return event.date > timezone.now()

def is_capacity_valid(capacity):
    """Vérifie que la capacité est positive"""
    return capacity > 0
