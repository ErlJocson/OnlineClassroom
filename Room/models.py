from django.db import models
from UserAuth.models import CustomUser
import random
import string

def generateRandomId():
    while True:
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for i in range(8))
        
        try:
            roomId = Room.objects.get(roomId=password).exists()
        except:
            roomId = ''

        if not roomId:
            return password

class Room(models.Model):
    name = models.CharField(max_length=24)
    roomId = models.CharField(max_length=10, default=generateRandomId)
    teacher = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

class ListOfStudent(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE)