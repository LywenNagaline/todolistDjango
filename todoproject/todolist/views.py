from django.shortcuts import render, redirect
from django.urls import reverse_lazy

# Create your views here.
from django.http import HttpResponse
from django.views.generic import View, TemplateView, DetailView, ListView, CreateView

from todolist.models import Task
from todolist.forms import TaskForm
from todolist.serializers import TaskSerializer

from rest_framework import viewsets


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

class AddTaskView(CreateView):
    form_class = TaskForm
    success_url = '/todo/tasks/' #reverse_lazy('task:list')
    template_name = 'todolist/add_task.html'

def add_task(request):
    form = TaskForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/todo/tasks/')
    return render(request, 'todolist/add_task.html', {'form': form})

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by("title")
    serializer_class = TaskSerializer