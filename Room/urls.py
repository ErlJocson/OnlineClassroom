from django.urls import path
from .views import *

urlpatterns = [
    path('', homeView, name='home'),
    path('missing/', missingView, name='missing'),
    path('todo/', todoView, name='todo'),
    path('done/', doneView, name='done'),
]