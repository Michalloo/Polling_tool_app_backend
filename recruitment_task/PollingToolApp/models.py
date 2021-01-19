from django.db import models


class Response(models.Model):
    answer = models.CharField(max_length=150)
