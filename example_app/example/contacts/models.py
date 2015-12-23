from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=12)
    surname = models.CharField(max_length=12)
    birthdate = models.DateField()

class Place(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)