from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('toggle/<int:task_id>/', views.toggle_task, name='toggle_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('trash/', views.trash_bin, name='trash_bin'),
    path('restore/<int:task_id>/', views.restore_task, name='restore_task'),
    path('permanent-delete/<int:task_id>/', views.permanent_delete_task, name='permanent_delete_task'),
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('settings/', views.settings_view, name='settings'),
    path('register/', views.register, name='register'),
    path('batch-action/', views.batch_action, name='batch_action'),
] 