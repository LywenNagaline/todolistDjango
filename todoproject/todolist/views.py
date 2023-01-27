from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import View, TemplateView, DetailView, ListView

from todolist.models import Task

def index(request):
    return HttpResponse("Bienvenue sur l'application !")

class AboutView(TemplateView):
    template_name = "about.html"

class TasksView(ListView):
    template_name="todolist/task_list.html"
    model = Task

class TaskDetailView(DetailView):
    template_name = "todolist/task_detail.html"
    model = Task