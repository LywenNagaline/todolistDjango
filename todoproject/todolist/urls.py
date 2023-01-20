from django.urls import path
from todolist import views

urlpatterns = [
    path ('about/', views.AboutView.as_view()),
    path('tasks/', views.TasksView.as_view()),
    path('tasks/<int:task_id>', views.TaskDetailView.as_view(), name="task_detail")
]