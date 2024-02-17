from django.db import models

# Create your models here.

class todoItem(models.Model):
    title = models.TextField()
    description = models.TextField()
    createdDate = models.DateField()
    updatedDate = models.DateField(auto_now=True)
