from django.db import models

# Create your models here.

class Response(models.Model):
    answer = models.CharField(max_length=150)