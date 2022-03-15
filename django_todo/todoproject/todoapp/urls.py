from django.urls import path
from .views import todo_list, create_task, edit_task, delete_task

urlpatterns = [
    path('todo-list', todo_list, name='todo-list'),
    path('create', create_task, name='todo-create'),
    path('edit/<int:task_id>', edit_task, name='todo-edit'),
    path('delete/<int:task_id>', delete_task, name='todo-delete')
]
