from django import forms
from todolist.models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'deadline', 'done')
        #fields = '__all__'