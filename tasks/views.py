from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from tasks.forms import TaskForm,TaskModelForm,TaskDetailModelForm
from tasks.models import Employee,Task,TaskDetail,Project
from datetime import date
from django.db.models import Q,Count,Max,Min,Avg
from django.contrib import messages


def manager_dashboard(request):
     type =request.GET.get('type', 'all')
     print(type)

      

     counts = Task.objects.aggregate(
        total=Count('id'),
        completed=Count('id', filter=Q(status='COMPLETED')),
        in_progress=Count('id', filter=Q(status='IN_PROGRESS')),
        pending=Count('id', filter=Q(status='PENDING')),
    )
     # retriving task data
     base_query=Task.objects.select_related('details').prefetch_related('assigned_to')

     if type =='completed':
         tasks=base_query.filter(status='COMPLETED')
     if type =='in_progress':
         tasks=base_query.filter(status='IN_PROGRESS')
     if type =='pending':
         tasks=base_query.filter(status='PENDING')
     if type =='all':
         tasks=base_query. all()
            

     context ={
         "tasks": tasks,
          "counts": counts

         
     }


     return render(request, "dashboard/manager.html",context)

def users_dashboard(request):
     return render(request, "dashboard/users.html")


 
def test(request):
     context = {
           "names" :['rana','jim','juwel']
    
     }
        
     
     return render(request, "test.html", context)

def create_task(request):
    # employees = Employee.objects.all()
    task_form = TaskModelForm()  # For GET
    task_detail_form = TaskDetailModelForm()

    if request.method == "POST":
        task_form = TaskModelForm(request.POST)
        task_detail_form = TaskDetailModelForm(request.POST)

        if task_form.is_valid() and task_detail_form.is_valid():

            """ For Model Form Data """
            task = task_form.save()
            task_detail = task_detail_form.save(commit=False)
            task_detail.task = task
            task_detail.save()

            messages.success(request, "Task Created Successfully")
            return redirect('create-task')

    context = {"task_form": task_form, "task_detail_form": task_detail_form}
    return render(request, "task_form.html", context)

def update_task(request, id):
    task = Task.objects.get(id=id)
    task_form = TaskModelForm(instance=task)  # For GET

    if task.details:
        task_detail_form = TaskDetailModelForm(instance=task.details)

    if request.method == "POST":
        task_form = TaskModelForm(request.POST, instance=task)
        task_detail_form = TaskDetailModelForm(
            request.POST, instance=task.details)

        if task_form.is_valid() and task_detail_form.is_valid():

            """ For Model Form Data """
            task = task_form.save()
            task_detail = task_detail_form.save(commit=False)
            task_detail.task = task
            task_detail.save()

            messages.success(request, "Task Updated Successfully")
            return redirect('update-task', id)

    context = {"task_form": task_form, "task_detail_form": task_detail_form}
    return render(request, "task_form.html", context)

def delate_task(request,id):
    if request.method=='POST':
        task=Task.objects.get(id=id)
        task.delete()
        messages.success(request,'task deleted successfully')
        return redirect('manager-dashboard')
    
    else:
        messages.error(request,'Somthing went wrong')
        return redirect('manager-dashboard')





def view_task(request):
    projects = Project.objects.annotate(
     num_task =Count('task')
    ).order_by('num_task')
    return render(request,'show_task.html',{"projects":projects})