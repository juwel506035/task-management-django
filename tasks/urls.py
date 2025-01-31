# tasks/urls.py
from django.urls import path
from .views import manager_dashboard,users_dashboard,test, create_task, view_task,update_task, delate_task 

urlpatterns = [
    path('manager-dashboard/', manager_dashboard,name='manager-dashboard'),
    path('users-dashboard/', users_dashboard),
    path('test/', test),
    path('create-task/', create_task, name='create-task'),
    path('view_task/',view_task),
    path('update-task/<int:id>/', update_task, name='update-task'),
    path('delete-task/<int:id>/',  delate_task, name='delete-task'),
]
