import uuid
from django.db import models
from django.contrib.auth.models import User
from events.models import Event

class Ticket(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    is_used = models.BooleanField(default=False)
    payment_status = models.BooleanField(default=False)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"{self.uuid} - {self.event.name}"


class ScanLog(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    scanned_at = models.DateTimeField(auto_now_add=True)
    valid = models.BooleanField(default=True)

    def _str_(self):
        return f"Scan {self.ticket.uuid}"
