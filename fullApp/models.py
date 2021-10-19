from django.db import models

class Dsa(models.Model):
    category=models.CharField(max_length=30)
    link=models.CharField(max_length=1000)
    concepts=models.CharField(max_length=1000)