"""Определяет сериализаторы приложения 'api'."""

from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Сериализатор для задач приложения 'api'."""

    class Meta:
        """Мета-информация для сериализатора."""

        model = Task
        fields = ('id', 'title', 'description', 'completed')
