from django.test import TestCase
from django.utils import timezone
from .models import Event

class EventModelTest(TestCase):

    def test_event_creation(self):
        event = Event.objects.create(
            name="Test Event",
            description="Test description",
            date=timezone.now() + timezone.timedelta(days=1),
            location="Rabat",
            capacity=100
        )
        self.assertEqual(event.name, "Test Event")
        self.assertTrue(event.capacity > 0)
