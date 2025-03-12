"""Конфигурация административного интерфейса для приложения 'api'."""

from django.contrib import admin

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    """Админка для задач."""

    list_display = ('title', 'description', 'completed')


admin.site.register(Task, TaskAdmin)
