from django import forms
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse_lazy
from .models import *


class ListForm(forms.ModelForm):

    class Meta:
        model = TodoList
        fields = ('list_title', 'list_priority')


class ItemForm(forms.ModelForm):

    class Meta:
        model = TodoItem
        fields = ('item_title', 'item_description', 'due', 'item_list')

    def __init__(self, *args, **kwargs ):
        super(ItemForm, self).__init__(*args, **kwargs)
        self.fields['item_list'].queryset = TodoList.objects.all()