from django.shortcuts import render
from django.utils import timezone
from .models import *


def item_list(request):
    items = TodoItem.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'todolist/item_items.html', {'items': items})