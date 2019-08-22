from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Project

# Create your views here.
class ProjectListView(ListView):
    template_name = 'project/project_list.html'

    def get_queryset(self):
        queryset = Project.objects.all()
        return queryset

class ProjectDetailView(DetailView):
    template_name = 'project/project_detail.html'

    def get_object(self):
        news_id = self.kwargs.get('id')
        return get_object_or_404(News, id=news_id)

def project_list(request, qty):
    projects = Project.objects.all()[:qty]
    return projects
