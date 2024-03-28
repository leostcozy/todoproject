from django.urls import path
from . import views
from .views import TaskList, TaskDetail

urlpatterns = [
    path("", TaskList.as_view(), name="taskList"),
    path("task/<int:pk>/", TaskDetail.as_view())
]
