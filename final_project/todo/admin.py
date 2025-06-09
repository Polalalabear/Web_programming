from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'completed', 'user')
    list_filter = ('completed', 'date', 'user')
    search_fields = ('title', 'description')
    ordering = ('date',)
