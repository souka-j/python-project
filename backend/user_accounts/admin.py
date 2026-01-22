from django.contrib import admin
from .models import Person


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'cin', 'birth_certificate_number')
    search_fields = ('first_name', 'last_name', 'cin')