from django import forms
from .models import *


class DateInput(forms.DateInput):
    input_type = 'date'


class ListForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = ('list_title', 'list_priority')


class ItemForm(forms.ModelForm):
    class Meta:
        model = TodoItem
        fields = ('item_title', 'item_description', 'due', 'done')
        widgets = {'due': DateInput(attrs={'class': 'datepicker'})}
