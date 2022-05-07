import random
import string

def generateRandomId():
    while True:
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for i in range(8))
        roomId = Room.objects.get(roomId=password).exists()
        if not roomId:
            return password