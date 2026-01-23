from django.test import TestCase
from django.contrib.auth.models import User
from events.models import Event
from .models import Ticket


class TicketModelTest(TestCase):

    def setUp(self):
        # utilisateur test
        self.user = User.objects.create_user(
            username="testuser",
            password="test1234"
        )

        # event test
        self.event = Event.objects.create(
            title="Match Test",
            location="Casablanca",
            date="2026-06-10"
        )

        # ticket test
        self.ticket = Ticket.objects.create(
            event=self.event,
            user=self.user,
            category="VIP",
            price=1200,
            quantity=1,
            payment_status="paid",
            description="Ticket VIP Match Test"
        )

    def test_ticket_creation(self):
        """Le ticket est bien créé"""
        self.assertEqual(self.ticket.price, 1200)
        self.assertEqual(self.ticket.category, "VIP")
        self.assertEqual(self.ticket.payment_status, "paid")
