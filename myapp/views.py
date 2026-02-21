import json
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateNewTask, CreateNewProject

# Create your views here.
def index(request):
    title = 'TaskFlow – Project & Task Manager!!'
    return render(request, 'index.html', {
        'title': title
    })

def about(request):
    username = 'Juan'
    return render(request, 'about.html', {
        'username': username
    })

def hello(request, username):
    return HttpResponse('Hello, %s!' %username)

def projects(request):
    # projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, 'projects/projects.html', {
        'projects': projects
    })

def tasks(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/tasks.html', {
        'tasks': tasks
    })

def create_task(request):
    if request.method == 'GET':
        return render(request, 'tasks/task_form.html', {
            'form': CreateNewTask   
        })
    else:
        Task.objects.create(
            title=request.POST['title'], 
            description=request.POST['description'], 
            project_id=request.POST['project_id']
        )
        return redirect('tasks')
    
def edit_task(request, id):
    if request.method == 'GET':    
        task = Task.objects.get(id=id)
        form = CreateNewTask(initial={
            'title': task.title,
            'description': task.description,
            'project_id': task.project_id,
        })
        return render(request, 'tasks/task_form.html', {
            'form': form,
            'editing': True,
        })
    else:
        task = Task.objects.get(id=id)
        task.title=request.POST['title']
        task.description=request.POST['description']
        task.project_id=request.POST['project_id']
        task.save()
        return redirect('tasks')

    
# def edit_task(request, id):
#     if request.method == "POST":
#         data = json.loads(request.body)
#         task = Task.objects.get(id=id)
#         task.title = data["title"]
#         task.save()

#         return JsonResponse({
#             "updated": True,
#             "title": task.title
#         })

def create_project(request):
    if request.method == 'GET':
        return render(request, 'projects/create_project.html', {
            'form': CreateNewProject
        })
    else:
        Project.objects.create(name=request.POST['name'])
        return redirect('projects')

def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    tasks = Task.objects.filter(project_id=id)
    return render(request, 'projects/detail.html', {
        'project': project,
        'tasks': tasks
    })

def toggle_task(request, id):
    if request.method == "POST":
        task = get_object_or_404(Task, id=id)
        task.done = not task.done
        task.save()
        return JsonResponse({"done": task.done})



def delete_task(request, id):
    if request.method == "POST":
        task = get_object_or_404(Task, id=id)
        task.delete()
        return JsonResponse({"deleted": True})