from django.db import models

class User(models.Model):
    email = models.EmailField(unique=True)           # Email unique
    name = models.CharField(max_length=100)          # Nom complet
    created_at = models.DateTimeField(auto_now_add=True)  # Date de création

    def __str__(self):
        return self.email
