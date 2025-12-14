from django.urls import path
from . import views


urlpatterns = [
path('tasks/', views.task_list),
path('create/', views.create_task),
path('complete/<int:task_id>/', views.complete_task),
]