import email
from email import message
from django.db import models

# Create your models here.

class Feedback(models.Model):
    name = models.CharField(max_length=34)
    email = models.EmailField( max_length=45)
    message = models.TextField()

    def __str__(self):
        return self.name