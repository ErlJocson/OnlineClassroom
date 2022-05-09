from django.contrib import admin
from .models import TeacherPost, PostComment, Work

admin.site.register(TeacherPost)
admin.site.register(PostComment)
admin.site.register(Work)