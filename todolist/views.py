from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import TodoItem
from .models import TodoList
from .forms import ItemForm
from .forms import ListForm
from django.shortcuts import render_to_response



def item_list(request):
    items = TodoItem.objects.order_by('due')
    return render(request, 'todolist/item_items.html', {'items': items})


def item_detail(request, pk):
    item = get_object_or_404(TodoItem, pk=pk)
    return render(request, 'todolist/item_detail.html', {'item': item})


@login_required
def item_new(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.author = request.user
            item.created_date = timezone.now()
            item.save()
            return redirect('item_detail', pk=item.pk)
    else:
        form = ItemForm()
    return render(request, 'todolist/item_edit.html', {'form': form})



@login_required
def item_edit(request, pk):
    item = get_object_or_404(TodoItem, pk=pk)
    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            item = form.save(commit=False)
            item.author = request.user
            item.modified_date = timezone.now()
            item.save()
            return redirect('item_detail', pk=item.pk)
    else:
        form = ItemForm(instance=item)
    return render(request, 'todolist/item_edit.html', {'form': form})


@login_required
def item_remove(request, pk):
    item = get_object_or_404(TodoItem, pk=pk)
    item.delete()
    return redirect('item_list')


@login_required
def item_toggle(request, pk, list_pk):
    item = get_object_or_404(TodoItem, pk=pk)
    item.done = not item.done
    item.save()
    list_detail(request, list_pk)
    return redirect('list_detail', pk=list_pk)


def list_list(request):
    lists = TodoList.objects.order_by('list_priority')
    return render(request, 'todolist/list_lists.html', {'lists': lists})


def list_detail(request, pk):
    list = get_object_or_404(TodoList, pk=pk)
    items = list.items.all()
    return render(request, 'todolist/list_detail.html', {'list': list, 'items': items})


@login_required
def list_new(request):
    if request.method == "POST":
        form = ListForm(request.POST)
        if form.is_valid():
            list = form.save(commit=False)
            list.author = request.user
            list.created_date = timezone.now()
            list.save()
            return redirect('list_detail', pk=list.pk)
    else:
        form = ListForm()
    return render(request, 'todolist/list_edit.html', {'form': form})



@login_required
def list_edit(request, pk):
    list = get_object_or_404(TodoList, pk=pk)
    if request.method == "POST":
        form = ListForm(request.POST, instance=list)
        if form.is_valid():
            list = form.save(commit=False)
            list.author = request.user
            list.modified_date = timezone.now()
            list.save()
            return redirect('list_detail', pk=list.pk)
    else:
        form = ListForm(instance=list)
    return render(request, 'todolist/list_edit.html', {'form': form})



@login_required
def list_remove(request, pk):
    list = get_object_or_404(TodoList, pk=pk)
    list.delete()
    return redirect('list_list')


def statistics(request):
    xdata = ["Apple", "Apricot", "Avocado", "Banana", "Boysenberries", "Blueberries", "Dates", "Grapefruit", "Kiwi",
             "Lemon"]
    ydata = [52, 48, 160, 94, 75, 71, 490, 82, 46, 17]

    extra_serie = {"tooltip": {"y_start": "", "y_end": " cal"}}
    chartdata = {'x': xdata, 'y1': ydata, 'extra1': extra_serie}
    charttype = "pieChart"

    data = {
        'charttype': charttype,
        'chartdata': chartdata,
    }

    return render_to_response(request, 'todolist/statistics.html', data)

