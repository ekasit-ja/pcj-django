from django.shortcuts import render
from .models import Project

# Create your views here.
def project_list(request, qty):
    return Project.objects.all()[:qty]
