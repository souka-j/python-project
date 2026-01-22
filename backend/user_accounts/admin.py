<<<<<<< HEAD
from django.contrib import admin
from .models import Person


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'cin', 'birth_certificate_number')
    search_fields = ('first_name', 'last_name', 'cin')
=======
from django.contrib import admin
from .models import Person


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'cin', 'birth_certificate_number')
    search_fields = ('first_name', 'last_name', 'cin')
>>>>>>> edb4cd70f90e28da79551583ab22fd1c3493f4ef
