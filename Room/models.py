from django.db import models
from UserAuth.models import UserClassification
from .functions import generateRandomId

class Room(models.Model):
    name = models.CharField(max_length=24)
    roomId = models.CharField(max_length=10, default=generateRandomId)
    teacher = models.ForeignKey(UserClassification, on_delete=models.CASCADE)

class ListOfStudent(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    student = models.ForeignKey(UserClassification, on_delete=models.CASCADE)