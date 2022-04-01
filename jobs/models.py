from django.db import models


# Create your models here.

class Job(models.Model):
    # images
    image = models.ImageField(upload_to='images/')
    # Summary
    summary = models.CharField(max_length=255)
