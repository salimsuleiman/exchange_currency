from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def Exchange(request):
    return render(request, 'exchange.html')


@login_required
def Home(request):
    return render(request, 'home.html')



def Profits(request):
    return render(request, 'profits.html')

def Warehouse(request):
    return render(request, 'quantity.html')