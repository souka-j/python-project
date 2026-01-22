
from rest_framework import generics
from .models import Event
from tickets.models import Ticket
from .serializers import EventSerializer, TicketSerializer

class EventListAPIView(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class TicketListAPIView(generics.ListAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
