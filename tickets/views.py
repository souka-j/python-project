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
