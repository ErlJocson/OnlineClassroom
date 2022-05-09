from django.urls import path
from .views import *

urlpatterns = [
    path('', homeView, name='home'),
    path('missing/', missingView, name='missing'),
    path('todo/', todoView, name='todo'),
    path('done/', doneView, name='done'),
    path('create-room/', createRoom, name='create-room'),
    path('view-room/<int:roomId>', roomView, name='room-view'),
]