from django.shortcuts import render
from django.shortcuts import HttpResponse
from tasks.forms import TaskForm,TaskModelForm
from tasks.models import Employee,Task

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
def view_task(request):
     # retrive all data from Task model
     tasks =Task.objects.all()
     # retrive spacic data from task model
     task_3 = Task.objects.get(pk=1)
     # fetch first task model
     first_task = Task.objects.first()
     return render(request, 'show_task.html',{'tasks': tasks, 'task3':task_3, 'first_task':first_task})
