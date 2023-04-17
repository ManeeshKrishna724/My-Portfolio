from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    projects = Project.objects.all()[0:3]
    return render(request, 'portfolio/index.html',context={
        "projects": projects
    })

def view_project(request,id):
    project = Project.objects.get(id=id)
    return render(request, 'portfolio/view-project.html',context=
                  {
        "project": project
                   }
                  )

def view_all_project(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/view-all-project.html',context={
        "projects": projects
    })