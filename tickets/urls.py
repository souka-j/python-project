from django.urls import path
from .views import scan_ticket

urlpatterns = [
    path("scan/", scan_ticket, name="scan-ticket"),
]
