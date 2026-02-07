from django.db import models
from django.conf import settings


class Meal(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    description = models.TextField()
    procedures = models.TextField()
    calories = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
