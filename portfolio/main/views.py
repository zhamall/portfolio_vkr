from django.shortcuts import render, get_object_or_404
from .models import Project, Tag, Resume

# Create your views here.

def home(request):
    resume = Resume.get_solo() 
    projects = Project.objects.all()
    tags = Tag.objects.all()
    return render(request, 'home.html', {"projects": projects, "tags": tags, "resume": resume})

def contact(request):
    resume = Resume.get_solo() 
    return render(request, 'contact.html', {"resume": resume})

def projects(request):
    projects = Project.objects.all()
    tags = Tag.objects.all()
    return render(request, 'projects.html', {"projects": projects, "tags": tags})

def project(request, id):
    project = get_object_or_404(Project, pk=id) 
    return render(request, 'project.html', {"project": project})

def resume_view(request):
    resume = Resume.get_solo()
    return render(request, 'resume.html', {'resume': resume})