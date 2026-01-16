from django.shortcuts import render
from .models import Ticket
from django.core.paginator import Paginator

def ticket_list(request):
    # Récupère tous les tickets
    all_tickets = Ticket.objects.all()
    
    # Met en pages 10 tickets par page
    paginator = Paginator(all_tickets, 10)
    page_number = request.GET.get('page')  # récupère le numéro de page depuis l'URL
    page_obj = paginator.get_page(page_number)
    
    # Envoie les tickets de la page au template
    return render(request, 'products/ticket_list.html', {'page_obj': page_obj})

