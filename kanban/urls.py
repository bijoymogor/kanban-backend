
from django.contrib import admin
from django.urls import path,include

from task import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/task/<int:pk>', views.task_api.as_view()),
    path('api/task/', views.task_api.as_view()),

]
