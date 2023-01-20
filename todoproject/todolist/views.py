from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import View, TemplateView

from todolist.models import Task

def index(request):
    return HttpResponse("Bienvenue sur l'application !")

class AboutView(TemplateView):
    template_name = "about.html"

class TasksView(TemplateView):
    template_name="todolist/task_list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tasks = Task.objects.all()
        context ["task_list"] = tasks
        return context

class TaskDetailView(TemplateView):
    template_name = "todolist/task_detail.html"
    def get_context_data(self, task_id, **kwargs):
        context = super().get_context_data(**kwargs)
        task = Task.objects.get(id=task_id)
        context ['task'] = task
        return context