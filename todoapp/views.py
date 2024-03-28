from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from .models import Task


class TaskList(ListView):
    model = Task
    context_object_name = "tasks"

class TaskDetail(DetailView):
    model = Task
    context_object_name = "task"
    
class TaskCreate(CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("taskList")

class TaskUpdate(UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("taskList")

class TaskDelete(DeleteView):
    model = Task
    success_url = reverse_lazy("taskList")
    context_object_name = "task"

class TaskLogin(LoginView):
    fields = "__all__"
    template_name = "todoapp/task_login.html"
    def get_success_url(self):
        return reverse_lazy("taskList")

