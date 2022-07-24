from django.contrib import admin
from .models import TaskTable


# Register your models here.
from django.contrib import admin
from .models import TaskTable


# Register your models here.

@admin.register(TaskTable)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id','project_id', 'task_id', 'Assignee','task_title','description', 'status', 'priority', 'deadline']
