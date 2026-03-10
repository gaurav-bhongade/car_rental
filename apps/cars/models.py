from django.db import models

# Create your models here.

class Car(models.Model):
    FUEL_CHOICES = [
        ('petrol', 'Petrol'),
        ('diesel', 'Diesel'),
        ('electric', 'Electric'),
        ('hybrid', 'Hybrid'),
    ]
    
    TRANSMISSION_CHOICES = [
        ('manual', 'Manual'),
        ('automatic', 'Automatic'),
    ]
    
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=50)
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    fuel_type = models.CharField(max_length=20, choices=FUEL_CHOICES)
    transmission = models.CharField(max_length=20, choices=TRANSMISSION_CHOICES)
    seats = models.PositiveIntegerField()
    image = models.ImageField(upload_to='cars/', blank=True, null=True)
    description = models.TextField()
    availability = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.brand} {self.name}"
