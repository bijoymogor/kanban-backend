from django.db import models

# Create your models here.


class TaskTable(models.Model):
    project_id = models.IntegerField()
    task_id = models.IntegerField()
    Assignee = models.CharField(max_length=500)
    task_title = models.CharField(max_length=500,blank=False, null=False)
    description = models.CharField(max_length=500)
    status = models.CharField(max_length=15)
    priority = models.CharField(max_length=2)
    deadline = models.CharField(max_length=15)

