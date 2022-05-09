from django.contrib.auth.models import User
from django.db import models

class TeacherPost(models.Model):
    title = models.CharField(max_length=24)
    description = models.TextField()
    posted = models.DateTimeField(auto_now_add = True)
    deadline = models.DateTimeField()
    toBeSubmitted = models.BooleanField(default=False)

class PostComment(models.Model):
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add = True)
    commentor = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(TeacherPost, on_delete=models.CASCADE)

class Works(models.Model):
    studentFile = models.FileField()
    grade = models.IntegerField()
    dataSubmitted = models.DateTimeField(auto_now_add = True)
    teacher = models.ForeignKey(TeacherPost, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)