from django.urls import path
from . import views
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete

urlpatterns = [
    path("", TaskList.as_view(), name="taskList"),
    path("task/<int:pk>/", TaskDetail.as_view(), name="task"),
    path("create-task/", TaskCreate.as_view(), name="taskCreate"),
    path("update-task/<int:pk>/", TaskUpdate.as_view(), name="taskUpdate"),
    path("delete-task/<int:pk>/", TaskDelete.as_view(), name="taskDelete"),
]

