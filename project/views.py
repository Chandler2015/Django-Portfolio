from django.shortcuts import render

from .models import Project


def home(request):
    projects = Project.objects
    return render(request, 'project/home.html', {'projects': projects})
