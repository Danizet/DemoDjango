# from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render, redirect
from .forms import CreateNewTask, CreateNewProject

# Create your views here.


def index(request):
    tittle = 'Aplicacion construccion'
    return render(request, "index.html", {
        'tittle': tittle
    })
    # return HttpResponse("Index page")
# Endclass


def about(request):
    username = "Lalavi"

    return render(request, "about.html", {
        'username': username
    })
    # return HttpResponse("About")
# enddef


def hello(request, username):
    return HttpResponse("<h1>Hello %s</h1>" % username)
# Enddef


def projects(request):
    # projects = list(Project.objects.values() )
    projects = Project.objects.all()
    return render(request, "project/projects.html", {
        'projects': projects
    })
    # return JsonResponse(projects, safe = False)
# enddef


def task(request):
    # task = Task.objects.get(id=id)
    # task = get_object_or_404(Task, id = id)
    tasks = Task.objects.all()
    return render(request, "task/task.html", {
        'tasks': tasks
    })
    # return HttpResponse('task: %s' % task.tittle)
# enddef


def create_task(request):
    if request.method == 'GET':
        return render(request, 'task/create_task.html', {
            'form': CreateNewTask()
        })
    else:
        Task.objects.create(
            tittle=request.POST['tittle'], description=request.POST['description'], project_id=2)
        return redirect('tasks')
    #EndiF
#Enddef


def create_project(request):
    if request.method == 'GET':
        return render(request, "project/create_project.html", {
            'forms': CreateNewProject
        })
    else:
        #print(request.POST)
        project = Project.objects.create(name = request.POST["name"])
        redirect('projects')
    #EndiF
#Enddef

def project_detail(request, id):
        #Project.objects.get(id=id)
        project = get_object_or_404(Project, id=id)
        tasks = Task.objects.filter(project_id=id)
        return render(request, 'projects/detail.html', {
            'project' : project,
            'tasks' : tasks,
        })
#Enddef

