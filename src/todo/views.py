from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Task
from .forms import TodoForm

def home(request):
    return render(request, "home.html")

class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = "todo/task_list.html" 
    

class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = "task"
    template_name = "todo/task_detail.html"

    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Task, id=id)
    

class TaskCreate(LoginRequiredMixin, CreateView):
    form_class = TodoForm
    template_name = "todo/task_create.html"
    success_url = reverse_lazy("todo:tasks")

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "The task was create succesfully")
        return super(TaskCreate, self).form_valid(form)

class TaskUpdate(LoginRequiredMixin, UpdateView):
    form_class = TodoForm
    template_name = "todo/task_update.html"
    success_url = reverse_lazy("todo:tasks")
    context_object_name = "task"

    def form_valid(self, form):
        messages.success(self.request, "The task was update successfully")
        return super(TaskUpdate, self).form_valid(form)
    def get_object(self):
        _id = self.kwargs.get("id")
        obj = get_object_or_404(Task, id=_id)
        return obj
    

class TaskDelete(LoginRequiredMixin, DeleteView):
    template_name = "todo/task_delete.html"
    success_url = reverse_lazy("todo:tasks")
    context_object_name = "task"
    model = Task

    def form_valid(self, form):
        messages.success(self.request, "The task was deleted successfully.")
        return super(TaskDelete,self).form_valid(form)

