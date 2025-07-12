# todo/urls.py

from django.urls import path
from . import views


urlpatterns = [
    path('', views.task_list, name='task-list'),
    path('create/', views.task_create, name='task-create'),
    path('toggle/<int:pk>/', views.task_toggle, name='task-toggle'),
    path('delete/<int:pk>/', views.task_delete, name='task-delete'),
]

