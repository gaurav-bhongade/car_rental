from django.db import models

# Create your models here.

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    image = models.ImageField(upload_to='team/', blank=True, null=True)
    social_links = models.JSONField(blank=True, null=True)  # e.g., {'facebook': 'url', 'twitter': 'url'}
    
    def __str__(self):
        return self.name
