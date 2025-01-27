from django.contrib import admin
from tasks.models import Employee, TaskDetail, Task, Project

# # Register your models here.
admin.site.register(Employee)
admin.site.register(TaskDetail)
admin.site.register(Task)
admin.site.register(Project)
