from django.db import models

class Ticket(models.Model):
    CATEGORY_CHOICES = [
        (1, 'Catégorie 1'),
        (2, 'Catégorie 2'),
        (3, 'Catégorie 3'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.IntegerField()
    category = models.IntegerField(choices=CATEGORY_CHOICES, default=1)

    def __str__(self):
        return f"{self.name} - Catégorie {self.category}"
