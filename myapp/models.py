from django.db import models

class DiseaseData(models.Model):
    location = models.CharField(max_length=255)
    disease_count = models.IntegerField()
    date = models.DateField()
