from django.db import models

# Create your models here.
class Feature(models.Model): # to inherit the properties of models from django
    name = models.CharField(max_length=50)
    details = models.CharField(max_length=400)
    completed = models.BooleanField(default = False)
    surname = models.CharField(max_length=50, default= 'Nkasi')
    
