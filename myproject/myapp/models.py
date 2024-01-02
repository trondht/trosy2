# Define models in Django /Python classes that define structure of database tables

from django.db import models
from django.conf import settings

class MenstrualCycle(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    symptoms = models.TextField(blank=True, null=True)

class TrainingSession(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField()
    duration = models.DurationField()
    intensity = models.CharField(max_length=50)
    type = models.CharField(max_length=100)
    notes = models.TextField(blank=True, null=True)

class GeneralHealthParameter(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField()
    parameter_name = models.CharField(max_length=100)
    value = models.CharField(max_length=100)

    


    