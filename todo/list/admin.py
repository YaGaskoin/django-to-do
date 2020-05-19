from django.contrib import admin
from .models import Task

# Register your models here.


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'deadline', 'priority', 'status']
    list_filter = ['created', 'deadline', 'priority', 'status']
    search_fields = ['name']