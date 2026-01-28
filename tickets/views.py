from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Ticket
from .services import validate_ticket
@api_view(["POST"])
def scan_ticket(request):
    uuid = request.data.get("uuid")
 if not uuid:
        return Response({"valid": False, "message": "UUID required"}, status=400)
 try:
        ticket = Ticket.objects.get(uuid=uuid)
    except Ticket.DoesNotExist:
        return Response({"valid": False, "message": "Ticket not found"}, status=404)
 if validate_ticket(ticket):
        return Response({"valid": True, "message": "Ticket valid"})
    else:
        return Response({"valid": False, "message": "Ticket already used"})
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from events.models import Event
from decimal import Decimal
def event_list(request):
    """Page publique avec tous les événements"""
    events = Event.objects.all()
    return render(request, 'tickets/event_list.html', {'events': events})
def buy_ticket(request, event_id):
    """Page pour acheter un ticket"""
    event = get_object_or_404(Event, id=event_id)
     if request.method == 'POST':  
        return redirect('ticket_confirmation', ticket_id=ticket.id)
     return render(request, 'tickets/buy_ticket.html', {'event': event})
def ticket_confirmation(request, ticket_id):
    """Page de confirmation d'achat"""
    ticket = get_object_or_404(Ticket, id=ticket_id)
    return render(request, 'tickets/ticket_confirm.html', {'ticket': ticket})

def my_tickets(request):
    """Page pour voir ses tickets"""
    if request.user.is_authenticated:
        tickets = Ticket.objects.filter(user=request.user)
    else:
        tickets = []
    
    return render(request, 'tickets/my_tickets.html', {'tickets': tickets})
