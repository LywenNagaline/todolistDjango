from django.urls import path
from todolist import views

urlpatterns = [
    path ('about/', views.AboutView.as_view())
]