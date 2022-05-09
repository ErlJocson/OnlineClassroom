from django.db import models
from django.contrib.auth.models import User
import random
import string

def generateRandomId():
    while True:
        characters = string.ascii_letters + string.digits 
        password = ''.join(random.choice(characters) for i in range(10))
        if not Room.objects.filter(roomId=password):
            return password

class Room(models.Model):
    name = models.CharField(max_length=24)
    roomId = models.CharField(max_length=10, default=generateRandomId)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)

class ListOfStudent(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)