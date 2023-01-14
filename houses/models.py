from django.db import models

# Create your models here.
class House(models.Model):
    """Model definition for house model"""
    name = models.CharField(max_length=140)
    price = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(max_length=140)
    pets_allowed = models.BooleanField(default=True, help_text="Does this house allow pets?",verbose_name="Pets allowed?")