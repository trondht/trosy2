from django.db import models
from django.conf import settings
from django.contrib.auth.models import User



class MenstrualCycle(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    symptoms = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Cycle starting on {self.start_date} for {self.user.username}"
    
class TrainingSession(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField()
    duration = models.DurationField()  # Could be in minutes or hours
    intensity = models.CharField(max_length=50)  # e.g., Low, Medium, High
    type = models.CharField(max_length=100)  # e.g., Cardio, Strength, Yoga
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.type} session on {self.date} for {self.user.username}"
    


    