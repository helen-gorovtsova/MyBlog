from datetime import datetime

from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class TodoList(models.Model):
    title = models.CharField(
        blank=True,
        max_length=50
    )

    content = models.CharField(
        blank=True,
        max_length=250
    )

    created = models.DateTimeField(
        default=datetime.now()
    )

    deadline = models.DateTimeField(
        default=datetime.now()
    )

    category = models.ForeignKey(
        Category,
        blank=True,
        on_delete=models.PROTECT,
        null=True,
        related_name='task'
    )

    status = models.CharField(
        blank=True,
        editable=False,
        default='Не начато',
        max_length=25
    )

    class Meta:
        verbose_name = 'Список задач'
        ordering = ['-created']

    def __str__(self):
        return self.title