from django.shortcuts import render
from django.shortcuts import HttpResponse

# views ar vitor amra logical kaj kore thaki

# Create your views here.
# views use kore ja kaj kora jai 
# work with database
# transform data
# data pass
# http response / json response

def home(request):
    return HttpResponse("<h1 style='color: red'>Welcome to the Task Management System</h1>")


def contact(resquest):
    return HttpResponse("This is contact page")
# tasks/views.py
def show_task(request):
    return HttpResponse("This is the Show Task Page")

def dashboard(request,id):
    return HttpResponse("This is Dashborad")
