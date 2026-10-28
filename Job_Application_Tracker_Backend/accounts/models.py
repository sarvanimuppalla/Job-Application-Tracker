from django.db import models
from django.utils import timezone

# Create your models here.
class accounts(models.Model):
    username = models.CharField(max_length=100, blank=False, unique=True)
    email = models.EmailField(unique=True )
    password = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)