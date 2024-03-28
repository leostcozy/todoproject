from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Task


class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = "tasks"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tasks"] = context["tasks"].filter(user=self.request.user)
        
        searchInputText = self.request.GET.get("search", "")
        if searchInputText:
            context["tasks"] = context["tasks"].filter(
                title__icontains=searchInputText
            )
        context["search"] = searchInputText
        return context
    
    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)

class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = "task"
    
class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ["title", "description", "completed"]
    success_url = reverse_lazy("taskList")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("taskList")

class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy("taskList")
    context_object_name = "task"

class TaskLogin(LoginView):
    fields = "__all__"
    template_name = "todoapp/task_login.html"
    def get_success_url(self):
        return reverse_lazy("taskList")

class RegisterTodoApp(FormView):
    form_class = UserCreationForm
    template_name = "todoapp/register.html"
    success_url = reverse_lazy("taskList")

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)

