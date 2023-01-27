from django.db import models


# Create your models here.
class TaskList (models.Model):
    name = models.CharField(max_length=255)
    def __str__(self) -> str:
        return  f"{self.name}"

class Task(models.Model):
    title = models.CharField(max_length=255)
    deadline = models.DateField(null=True, blank=True)
    done = models.BooleanField()
    task_list = models.ForeignKey(
        TaskList, null=True, blank=True,
        on_delete=models.CASCADE
        )
    def __str__(self) -> str:
        return  f"{self.title}"

