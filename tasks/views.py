from django.shortcuts import render
from django.shortcuts import HttpResponse
from tasks.forms import TaskForm,TaskModelForm
from tasks.models import Employee,Task,TaskDetail,Project
from datetime import date
from django.db.models import Q,Count,Max,Min,Avg


# views ar vitor amra logical kaj kore thaki

# Create your views here.
# views use kore ja kaj kora jai 
# work with database
# transform data
# data pass
# http response / json response

def manager_dashboard(request):
     return render(request, "dashboard/manager.html")

def users_dashboard(request):
     return render(request, "dashboard/users.html")


 
def test(request):
     context = {
           "names" :['rana','jim','juwel']
    
     }
        
     
     return render(request, "test.html", context)

def create_task(request):
    form = TaskModelForm()  # Initialize the form for GET requests

    if request.method == 'POST':
        form = TaskModelForm(request.POST)
        if form.is_valid():
            form.save()  # Save the task to the database
            # Pass a success message to the context
            context = {'form': form, 'message': 'Task added successfully'}
            return render(request, 'task_form.html', context)
        
            # for django form data
            # data = form.cleaned_data
            # title = data.get('title')
            # description = data.get('description')
            # due_date = data.get('due_date')
            # assigned_to = data.get('assigned_to')
            # print(title, description, due_date, assigned_to)

            # # Create a new task
            # task = Task.objects.create(
            #     title=title, description=description, due_date=due_date
            # )

            # # Assign the task to selected employees
            # for emp_id in assigned_to:
            #     employee = Employee.objects.get(id=emp_id)
            #     task.assigned_to.add(employee)

            # return HttpResponse("Task Added Successfully")

    context = {'form': form}
    return render(request, "task_form.html", context)  # Pass 'form' in the context

# retrive data 
# def view_task(request):
#      # retrive all data from Task model
#      tasks =Task.objects.all()
#      # retrive spacic data from task model
#      task_3 = Task.objects.get(pk=1)
#      # fetch first task model
#      first_task = Task.objects.first()
#      return render(request, 'show_task.html',{'tasks': tasks, 'task3':task_3, 'first_task':first_task})

# filter using jkhn multi data dekhte caibo
# def view_task(request):
#      # tasks = Task.objects.filter(status='PENDING')
#      # show the task which due date is today
#      # tasks =Task.objects.filter(due_date=date.today())
#      '''show the task whose priority is not Low'''
#      # tasks = TaskDetail.objects.exclude(priority='L')
#      # return render(request, 'show_task.html',{'tasks':tasks})


# using filter ar lookups:
# def view_task(request):
      
#      '''show the task that contain word "paper"'''
#      # tasks =Task.objects.filter(title__icontains ="c",status='PENDING')
#      '''show the task which are pending and in progress'''
#      tasks =Task.objects.filter(Q(status='PENDING')| Q(status='IN_PROGRESS'))
#      return render(request, 'show_task.html',{"tasks": tasks})

# select_related (foreignkey, oneTonneField)
# def view_task(request):
     # tasks=Task.objects.select_related('details').all()
     # tasks=TaskDetail.objects.select_related('task').all()
     # tasks=Task.objects.select_related('project').all()

     # '''prefetch_related(foreignkey many to many relation)'''
     # tasks = Project.objects.prefetch_related('task_set').all()
     # many to many
     # tasks =Task.objects.prefetch_related('assigned_to').all()
     # print(tasks)
     # return render(request, 'show_task.html',{"tasks": tasks})

def view_task(request):
    projects = Project.objects.annotate(
     num_task =Count('task')
    ).order_by('num_task')
    return render(request,'show_task.html',{"projects":projects})