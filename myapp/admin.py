from django.contrib import admin
from .models import DiseaseData  # Replace `YourModel` with your actual model name(s)

# Register your models here.
admin.site.register(DiseaseData)  # Repeat this for each model you want to register
