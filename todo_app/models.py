from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Task(models.Model):
    title = models.TextField()
    description = models.TextField(null=False, blank=True)
    completed = models.BooleanField(default=False, blank=True, null=True)
    createdDate = models.DateTimeField(default=timezone.now)

class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    email = models.CharField(max_length=249, null=True, blank=True, unique=True)
    username = models.CharField(max_length=200, null=True, blank=True)
    password = models.CharField(max_length=200)

