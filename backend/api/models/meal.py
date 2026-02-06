from django.conf import settings
from django.db import models

class Meal(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,  on_delete=models.CASCADE)
    title = models.CharField(max_length=67)
    description = models.TextField()
    procedures = models.TextField()
    calories = models.FloatField()
    generated_at = models.DateTimeField(auto_now_add=True)

