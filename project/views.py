from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.views.generic.edit import FormMixin
from django.http import JsonResponse
from django.utils.translation import get_language
from django.core.paginator import Paginator
from django.utils.translation import gettext as _

from .models import Project
from .forms import ProjectForm

# Create your views here.
class ProjectListView(FormMixin, ListView):
    template_name = 'project/project_list.html'
    context_object_name = 'project_queryset'
    form_class = ProjectForm

    def get_initial(self):
        return {
            'country': self.request.GET.get('country'),
            'year': self.request.GET.get('year'),
        }

    def get_queryset(self):
        queryset = Project.objects.all()
        year = self.request.GET.get('year')
        country = self.request.GET.get('country')

        if year and year != 'all':
            queryset = queryset.filter(year=year)

        if country and country != 'all':
            queryset = queryset.filter(country=country)

        paginator = Paginator(queryset, 15)
        page = self.request.GET.get('page')
        queryset = paginator.get_page(page)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['meta_title'] = _('projects').capitalize()
        context['meta_robots'] = 'index, nofollow'
        return context

def project_detail(request, id):
        project = Project.objects.filter(id=id)
        p = project.first()
        values = {}

        if p:
            values = project.values().first()
            values['title'] = p.title
            values['image'] = p.image.url
            del values['title_en']
            del values['title_th']
            del values['order']

        return JsonResponse(values)

def project_list(request, qty):
    projects = Project.objects.all()[:qty]
    return projects
