from django.contrib.auth.models import User
from django.db import models
from Room.models import Room

class TeacherPost(models.Model):
    title = models.CharField(max_length=24)
    description = models.TextField()
    posted = models.DateTimeField(auto_now_add = True)
    theFile = models.FileField(upload_to='teacher-files/' ,blank=True)
    deadline = models.DateTimeField()
    toBeSubmitted = models.BooleanField(default=False)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    
class PostComment(models.Model):
    comment = models.TextField()
    posted = models.DateTimeField(auto_now_add = True)
    commentor = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(TeacherPost, on_delete=models.CASCADE)

class Work(models.Model):
    studentFile = models.FileField(upload_to='student-files/', blank=True)
    grade = models.IntegerField(blank=True)
    dataSubmitted = models.DateTimeField(auto_now_add = True)
    teacher = models.ForeignKey(TeacherPost, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    graded = models.BooleanField(default=False)