from django.urls import path
from .views import EventListAPIView, TicketListAPIView

urlpatterns = [
    path('api/events/', EventListAPIView.as_view(), name='api-events'),
    path('api/tickets/', TicketListAPIView.as_view(), name='api-tickets'),
]
