from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    nameExtension = models.CharField(max_length=10)
    email = models.EmailField(max_length=254)
    isTeacher = models.BooleanField(blank=True, null=True)
    isStudent = models.BooleanField(blank=True, null=True)