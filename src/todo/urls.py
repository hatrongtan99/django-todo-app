from django.urls import path
from . import views

app_name = "todo"

urlpatterns = [
    path("", views.home, name="home"),
    path("tasks/", views.TaskList.as_view(), name="tasks"),
    path("tasks/<int:id>/", views.TaskDetail.as_view(), name="task"),
    path("tasks/create/", views.TaskCreate.as_view(), name="create"),
    path("tasks/update/<int:id>/", views.TaskUpdate.as_view(), name="update"),
    path("tasks/delete/<int:pk>/", views.TaskDelete.as_view(), name="delete")
]