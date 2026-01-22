<<<<<<< HEAD
from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    cin = models.CharField(
        max_length=20,
        unique=True,
        null=True,
        blank=True,
        help_text="Carte Nationale (obligatoire pour adultes)"
    )
    birth_certificate_number = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        help_text="Acte de naissance (pour enfants/bébés)"
    )
    photo = models.ImageField(
        upload_to='persons_photos/',
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

=======
from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    cin = models.CharField(
        max_length=20,
        unique=True,
        null=True,
        blank=True,
        help_text="Carte Nationale (obligatoire pour adultes)"
    )
    birth_certificate_number = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        help_text="Acte de naissance (pour enfants/bébés)"
    )
    photo = models.ImageField(
        upload_to='persons_photos/',
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
>>>>>>> edb4cd70f90e28da79551583ab22fd1c3493f4ef
