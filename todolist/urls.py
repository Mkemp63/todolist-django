from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.list_list, name='list_list'),
    path('item', views.item_list, name='item_list'),
    path('item/<int:pk>/', views.item_detail, name='item_detail'),
    path('item/new/', views.item_new, name='item_new'),
    path('item/<int:pk>/edit/', views.item_edit, name='item_edit'),
    path('item/<int:pk>/remove/', views.item_remove, name='item_remove'),
    path('list/<int:pk>/', views.list_detail, name='list_detail'),
    path('list/new/', views.list_new, name='list_new'),
    path('list/<int:pk>/edit/', views.list_edit, name='list_edit'),
    path('list/<int:pk>/remove/', views.list_remove, name='list_remove'),




]