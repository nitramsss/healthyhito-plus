from django.conf import settings
from django.db import models

class Notification(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,  on_delete=models.CASCADE)
    message = models.CharField(max_length=544)
    sent_at = models.DateTimeField(auto_now_add=True)
    read_at = models.DateTimeField(null=True)

