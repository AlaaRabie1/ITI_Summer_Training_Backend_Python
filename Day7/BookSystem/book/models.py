from django.db import models

# Create your models here.
class Book:
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=3)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title