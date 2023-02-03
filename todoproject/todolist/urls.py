from django.urls import path, include
from todolist import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'todolist', views.TaskViewSet)

urlpatterns = [
    path ('about/', views.AboutView.as_view()),
    path('tasks/', views.TasksView.as_view(), name="tasks_list"),
    path('tasks/<int:task_id>', views.TaskDetailView.as_view(), name="task_detail"),
    path('add_task/', views.AddTaskView.as_view(), name="add_task"),
    path('api/v1/', include(router.urls)),
    path('api/v0/tasks/', views.APITaskView.as_view()),
    path('api/v0/tasks/<int:id>', views.APITaskDetailView.as_view())
]