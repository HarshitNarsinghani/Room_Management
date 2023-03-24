from django.urls import path
from .views import available_rooms

urlpatterns = [
    path('available-rooms/',available_rooms,name='available-rooms'),
]
