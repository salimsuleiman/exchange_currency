

from django.urls import path

from .views  import *

urlpatterns = [
   
    path('rates/', Rates),
    path('add/', add),
    path('exchange/', exchange),
    path('warehouse/', warehouse),
    path('reciepts/', reciepts),
    path('store/add/', store_add),
    path('store/edit/<int:ID>/', store_edit),
    path('delete/<int:ID>/', delete),
    path('edit/<int:ID>/', edit),

]
