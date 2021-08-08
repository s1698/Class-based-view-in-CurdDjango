from django.db import models
from django.urls import reverse
# Create your models here.

class Member(models.Model):
    firstname = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    
    def get_absolute_url(self):
        return reverse('index')

    def __str__(self):
        return self.firstname + " " + self.lastname