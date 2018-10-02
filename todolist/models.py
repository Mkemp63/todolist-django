from django.db import models
from django.utils import timezone


class TodoList(models.Model):
    list_title = models.CharField(max_length=30)
    list_priority = models.IntegerField()
    modified_date = models.DateTimeField(
        default=timezone.now)
    created_date = models.DateTimeField(
        default=timezone.now)

    class Meta:
        verbose_name = "TodoItem"
        verbose_name_plural = "TodoItems"
        ordering = ["list_priority"]

    def __str__(self):
        return self.list_title


class TodoItem(models.Model):
    item_title = models.CharField(max_length=200)
    item_description = models.TextField(max_length=200, null=True, blank=True)
    item_list = models.ForeignKey(TodoList, on_delete=models.DO_NOTHING, blank=True, null=True)
    due = models.DateTimeField(null=True, blank=True)
    done = models.BooleanField(default=False)
    modified_date = models.DateTimeField(
            default=timezone.now, null=True, blank=True)
    created_date = models.DateTimeField(
            default=timezone.now)

    class Meta:
        ordering = ["due"]

    def __str__(self):
        return self.item_title


