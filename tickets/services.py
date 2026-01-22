from .models import Ticket, ScanLog

def validate_ticket(ticket: Ticket):
    if ticket.is_used:
        ScanLog.objects.create(ticket=ticket, valid=False)
        return False

    ticket.is_used = True
    ticket.save()
    ScanLog.objects.create(ticket=ticket, valid=True)
    return True
