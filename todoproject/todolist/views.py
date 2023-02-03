from django.shortcuts import render, redirect
from django.urls import reverse_lazy

# Create your views here.
from django.http import HttpResponse
from django.views.generic import View, TemplateView, DetailView, ListView, CreateView

from todolist.models import Task
from todolist.forms import TaskForm
from todolist.serializers import TaskSerializer

from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authtoken.models import Token

from django.core.exceptions import ObjectDoesNotExist

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

class APITaskView(APIView):
    def get(self, request, format=None):
        tasks_list = Task.objects.all()
        serializer = TaskSerializer(tasks_list, many=True)
        response_data = {"results": serializer.data}
        return Response(response_data)

    def post(self, request, format=None):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class APITaskDetailView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self, request, id, format=None):
        task = Task.objects.get(id=id)
        serializer = TaskSerializer(task)
        response_data = {"results": serializer.data}
        return Response(response_data)
    
    def delete(self, request, id, format=None):
        try:
            task = Task.objects.get(id=id)
            task.delete()
        except ObjectDoesNotExist:
             return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, id, format=None):
        try:
            task = Task.objects.get(id=id)
            serializer = TaskSerializer(task, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
             return Response(status=status.HTTP_404_NOT_FOUND)
