from django.db import models

# Create your models here.

class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=50, blank=True, null=True)  # e.g., 'fa-car' for fontawesome
    image = models.ImageField(upload_to='services/', blank=True, null=True)
    
    def __str__(self):
        return self.title
