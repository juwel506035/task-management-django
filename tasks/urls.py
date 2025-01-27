# tasks/urls.py
from django.urls import path
from .views import manager_dashboard,users_dashboard,test,create_task,view_task

urlpatterns = [
    path('manager-dashboard/', manager_dashboard),
    path('users-dashboard/', users_dashboard),
    path('test/', test),
    path( 'create-task/', create_task),
    path('view_task/',view_task)
]
