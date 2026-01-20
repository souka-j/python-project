from django.urls import path
from .views import list_events, create_event

urlpatterns = [
    path('', list_events, name='list_events'),
    path('create/', create_event, name='create_event'),
]
