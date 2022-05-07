from django.db import models
from UserAuth.models import UserClassification
import random
import string

def generateRandomId():
    while True:
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for i in range(8))
        roomId = Room.objects.get(roomId=password).exists()
        if not roomId:
            return password

class Room(models.Model):
    name = models.CharField(max_length=24)
    roomId = models.CharField(max_length=10, default=generateRandomId)
    teacher = models.ForeignKey(UserClassification, on_delete=models.CASCADE)