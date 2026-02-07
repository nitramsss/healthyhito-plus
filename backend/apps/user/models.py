from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    height = models.FloatField()
    weight = models.FloatField()
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    REQUIRED_FIELDS = ['height', 'weight', 'age']

    def __str__(self) -> str:
        return f'{self.username}'
