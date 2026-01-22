<<<<<<< HEAD
from django.shortcuts import render
from .models import Person


def persons_list(request):
    persons = Person.objects.all()
    return render(request, 'persons_list.html', {'persons': persons})
=======
from django.shortcuts import render
from .models import Person


def persons_list(request):
    persons = Person.objects.all()
    return render(request, 'persons_list.html', {'persons': persons})
>>>>>>> edb4cd70f90e28da79551583ab22fd1c3493f4ef
