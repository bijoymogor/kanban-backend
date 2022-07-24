from rest_framework import serializers
from task.models import TaskTable


class TaskSerializers(serializers.ModelSerializer):
    class Meta:
        model = TaskTable
        fields = ['id','project_id','task_id','Assignee','task_title','description','status','priority','deadline']