from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    place = models.CharField(max_length=100, null=True, blank=True)
    mobile = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='image', null=True, blank=True)


def __str__(self):
    return self.name()