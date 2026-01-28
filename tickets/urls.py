from django.urls import path
from .views import scan_ticket

urlpatterns = [
    path("scan/", scan_ticket, name="scan-ticket"),
]
from django.urls import path
from .views import scan_ticket, event_list, buy_ticket, ticket_confirmation, my_tickets


urlpatterns = [
    # pour garder url
    path("scan/", scan_ticket, name="scan-ticket"),
   path("events/", event_list, name="event_list"),
    path("buy/<int:event_id>/", buy_ticket, name="buy_ticket"),
    path("confirmation/<int:ticket_id>/", ticket_confirmation, name="ticket_confirmation"),
    path("my-tickets/", my_tickets, name="my_tickets"),
]
