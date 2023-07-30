from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('update-task/<str:pk>/', update_task, name="update_task"),
    path('delete-task/<str:pk>/', delete_task, name="delete_task"),
]
