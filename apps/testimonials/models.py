from django.db import models

# Create your models here.

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    review = models.TextField()
    rating = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)])  # 1 to 5 stars
    image = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    
    def __str__(self):
        return f"Testimonial by {self.name}"
