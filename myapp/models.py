import email
from unicodedata import name
from django.db import models

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=330)

    def __str__(self) -> str:
        return self.name