from django.contrib import admin
from .models import Ticket, ScanLog

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'event', 'user', 'price', 'is_used', 'payment_status')
    search_fields = ('uuid',)

@admin.register(ScanLog)
class ScanLogAdmin(admin.ModelAdmin):
    list_display = ('ticket', 'scanned_at', 'valid')
  
