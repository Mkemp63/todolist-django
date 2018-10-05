from django.db import models
from django.utils import timezone


class TodoList(models.Model):
    list_title = models.CharField(max_length=30, null=False)
    list_priority = models.IntegerField(null=False)
    modified_date = models.DateTimeField(
        default=timezone.now)
    created_date = models.DateTimeField(
        default=timezone.now)

    class Meta:
        ordering = ["list_priority"]

    def __str__(self):
        return self.list_title


class TodoItem(models.Model):
    item_title = models.CharField(max_length=200, null=False, blank=False)
    item_description = models.TextField(max_length=200, null=True, blank=True)
    item_list = models.ForeignKey(TodoList, related_name="items", on_delete=models.CASCADE, null=False, default=1)
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
