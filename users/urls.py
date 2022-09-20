

from django.urls import path

from .views  import *

urlpatterns = [
   
    path('', Users),
    path('add/', add),
    path('profile/', profile),
    path('login/', login_page, name="login"),
    path('logout/', Logout),
    path('edit/<int:ID>/', edit),
    path('delete/<int:ID>/', delete),

]
