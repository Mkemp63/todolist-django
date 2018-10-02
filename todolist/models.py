from django.db import models
from django.utils import timezone


class TodoItem(models.Model):
    item_title = models.CharField(max_length=200)
    item_description = models.TextField(max_length=200, null=True, blank=True)
    due = models.DateTimeField(null=True, blank=True)
    modified_date = models.DateTimeField(
            default=timezone.now, null=True, blank=True)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.item_title


class TodoList(models.Model):
    list_title = models.CharField(max_length=30)
    list_priority = models.IntegerField()
    list_items = models.ForeignKey(TodoItem, on_delete=models.CASCADE, related_name="list", null=True, blank=True)
    modified_date = models.DateTimeField(
        default=timezone.now)
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.list_title

