from django.db import models

# Create your models here.

class Exam(models.Model):
    name = models.CharField(max_length=100, null=True)
    age = models.IntegerField(null=True)
    place = models.CharField(max_length=200, null=True)
    mobile = models.IntegerField(null=True, blank=False)
    email = models.EmailField(null=True)
    course = models.CharField(max_length=200)

def __str__(self):
    self.name() 
