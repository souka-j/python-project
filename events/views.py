from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.http import require_http_methods
from .models import Event
from .services import is_event_in_future, is_capacity_valid
import json

@require_http_methods(["GET"])
def list_events(request):
 
    events = Event.objects.all().values()
    return JsonResponse(list(events), safe=False)

@require_http_methods(["POST"])
def create_event(request):
   
    try:
        data = json.loads(request.body)

        event = Event(
            name=data['name'],
            description=data.get('description', ''),
            date=data['date'],
            location=data['location'],
            capacity=data['capacity']
        )

        if not is_capacity_valid(event.capacity):
            return HttpResponseBadRequest("Invalid capacity")

        event.save()
        return JsonResponse({"message": "Event created"}, status=201)

    except Exception as e:
        return HttpResponseBadRequest(str(e))

