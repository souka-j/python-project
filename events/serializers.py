from rest_framework import serializers
from .models import Event
from tickets.models import Ticket

# Serializer pour Event
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

# Serializer pour Ticket
class TicketSerializer(serializers.ModelSerializer):
    event = EventSerializer(read_only=True)  # Affiche l'event lié
    class Meta:
        model = Ticket
        fields = '__all__'
