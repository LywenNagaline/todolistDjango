from django.contrib import admin

from todolist.models import Task, TaskList

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'deadline' 'done')


admin.site.register(Task)
admin.site.register(TaskList)
# Register your models here.
