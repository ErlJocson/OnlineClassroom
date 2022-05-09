from django.urls import path
from .views import postView

urlpatterns = [
    path('post/', postView, name='post-view')
]