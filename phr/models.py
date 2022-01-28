from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PHR(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    email = models.EmailField(blank=True)
    tel_number = models.CharField(max_length=10, blank=False)
    citizen_id = models.CharField(max_length=13, blank=False)
    weight = models.FloatField(blank=False)
    height = models.FloatField(blank=False)
    pressure = models.CharField(max_length=10, blank=True)
    blood_group = models.CharField(max_length=5, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)