# tasks/urls.py
from django.urls import path
from .views import show_task

urlpatterns = [
    path('show_task/', show_task),
]
