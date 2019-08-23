from django.urls import path
from .views import (
    ProjectListView,
    project_detail,
)

app_name = 'project'
urlpatterns = [
    path('', ProjectListView.as_view(), name='project-list'),
    path('<int:id>/', project_detail, name='project-detail'),
]
