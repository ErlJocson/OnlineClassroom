from django.db import models
from django.contrib.auth.models import User

class UserClassification(models.Model):
    isTeacher = models.BooleanField()
    gender = models.CharField(max_length=10)
    user = models.ForeignKey(User, on_delete=models.CASCADE)