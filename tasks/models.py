from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()

class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True,default=True)
    description = models.TextField(null=True,default=True)
    due_date = models.DateField(null=True,default=True)
    status = models.CharField(max_length=20, choices=[
        ('PENDING', 'Pending'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed')
    ])
    is_completed = models.BooleanField(default=False)
    assigned_to = models.ManyToManyField(Employee)

class TaskDetail(models.Model):
    task = models.OneToOneField(Task, on_delete=models.CASCADE)
    assigned_to = models.TextField()
    priority = models.CharField(max_length=1, choices=[
        ('H', 'High'),
        ('M', 'Medium'),
        ('L', 'Low')
    ])
    notes = models.TextField()
