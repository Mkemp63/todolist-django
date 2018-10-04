from django import forms

from .models import *


class ListForm(forms.ModelForm):

    class Meta:
        model = TodoList
        fields = ('list_title', 'list_priority')


class ItemForm(forms.ModelForm):

    class Meta:
        model = TodoItem
        fields = ('item_title', 'item_list', 'item_description', 'due', 'done')

    def __init__(self, *args, **kwargs ):
        super(ItemForm, self).__init__(*args, **kwargs)
        self.fields['item_list'].queryset = TodoList.objects.all()

class SearchForm(forms.Form):
    q = forms.CharField(
        widget=forms.widgets.TextInput(attrs={'size': 35})
    )