from django.db import models

class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    mail = models.EmailField()
    address = models.TextField()
    district = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)
    acctype = models.CharField(max_length=50)
    material = models.CharField(max_length=50)