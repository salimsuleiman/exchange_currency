from locale import currency
from django.shortcuts import render, redirect
from users.models import User
from currencies.models import Currency, Store
from django.db import IntegrityError
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from decimal import *
from transactions.models import Transaction
from conversion import *

@login_required
def Rates(request):
    currencies = Currency.objects.all()
    return render(request, 'currencies/rate.html', {'currencies': currencies})

@login_required
def delete(request, ID):
    currency = Currency.objects.filter(id=ID).first()
    if request.method == "POST":
        if currency is None:
             return redirect('/currencies/rates/')
        else:
             currency.delete()
             return redirect('/currencies/rates/')

    return render(request, 'currencies/delete.html')

# can you see me ;) mxe how do i chat with you here?
# can you type? 
# i opened the home .html does it shows to you?
# See this? Salim
# yeah i did

# friggin cool man
#hello salim
# mxe shut up
# that's the views conversion file for the exchanges
@login_required
def edit(request, ID):
    currency = Currency.objects.filter(id=ID).first()
   
    if request.method == 'POST':
        name = request.POST['name']
        symbol = request.POST['symbol']
        buy_price = request.POST['buy_price']
        sell_price = request.POST['sell_price']

        try:
            if '' in (name, symbol, buy_price, sell_price):
                messages.add_message(request, messages.INFO, 'Please enter all fields =)')
                return redirect(f'/currencies/edit/{ID}/')
            currency.name=name
            currency.symbol=symbol
            currency.buy_price=buy_price
            currency.sell_price=sell_price
            currency.save()
            return  redirect('/currencies/rates/')
        except IntegrityError:
                messages.add_message(request, messages.INFO, 'Make sure name and symbol are unique')
        

    return render(request, 'currencies/edit.html', {'currency':currency})



@login_required
def add(request):
   name = request.POST['name']
   symbol = request.POST['symbol']
   buy_price = request.POST['buy_price']
   sell_price = request.POST['sell_price']

   try:
        if '' in (name, symbol, buy_price, sell_price):
            messages.add_message(request, messages.INFO, 'Please enter all fields =)')
            return redirect('/currencies/rates/')
        new = Currency.objects.create(name=name, symbol=symbol, buy_price=buy_price, sell_price=sell_price)
 
   except IntegrityError:
        messages.add_message(request, messages.INFO, 'Make sure name and symbol are unique')
        

   return redirect('/currencies/rates/')


def exchange(request):
    currencies = Currency.objects.all()
    if request.method == "POST":
        
       
        amount = request.POST['amount']
        currency = Currency.objects.filter(id=request.POST['currency']).first()
        currency_to = Currency.objects.filter(id=request.POST['currency_to']).first()
        if '' in (amount, currency, currency_to):
            return redirect('/currencies/exchange/')
        
        if currency.symbol != currency_to.symbol:
        
            if currency.symbol == 'IQD':
                
                money = local_to_foreing(amount, currency_to.sell_price)
                return render(request, 'currencies/exchange.html', {'currencies': currencies, 'money': money,  "symbol_to": currency_to.symbol})
            elif currency_to.symbol == "IQD":
                # it's a buy tx
                # money = float(amount)*float(currency.sell_price)
                money = foreing_to_local(amount, currency.buy_price)
                return render(request, 'currencies/exchange.html', {'currencies': currencies, 'money': money,  "symbol_to": currency_to.symbol})
        else:
            # can't convert same currency =)
            return redirect('/currencies/exchange/')

    return render(request, 'currencies/exchange.html', {'currencies': currencies})


def warehouse(request):
    currencies = Currency.objects.all()
    stores=Store.objects.all()

    return render(request, 'currencies/warehouse.html',  {'currencies': currencies, 'stores':stores})

def store_edit(request,ID):
    store = Store.objects.filter(id=ID).first()
    if store is None:
        return redirect('/currencies/warehouse/')
    currencies = Currency.objects.all()

    if request.method == 'POST':
        name = request.POST['name']
        price = request.POST['price']
        currency = request.POST['currency']

        c = Currency.objects.filter(id=currency).first()
        if c is None:
            return redirect('/currencies/warehouse/')
        if '' in (name, currency, price):
            messages.add_message(request, messages.INFO, 'الرجاء إدخال كافة الحقول')
            return redirect('/currencies/warehouse/')
        store.name=name
        store.price=price
        store.currency=c
        store.save()
        return redirect('/currencies/warehouse/')
       

    return render(request, 'currencies/store_edit.html', {'store':store, 'currencies':currencies})

def store_add(request):
    
    name = request.POST['name']
    price = request.POST['price']
    currency = request.POST['currency']

    if '' in (name, currency, price):
            messages.add_message(request, messages.INFO, 'الرجاء إدخال كافة الحقول')
            return redirect('/currencies/warehouse/')

    c = Currency.objects.filter(id=currency).first()
    if c is None:
        return redirect('/currencies/warehouse/')
    store = Store.objects.create(name=name, price=price, currency=c)
    return redirect('/currencies/warehouse/')


def reciepts(request):
    transactions = Transaction.objects.all()
    return  render(request, 'currencies/reciepts.html', {'transactions':transactions})



def profits(request):
    # profit = float(amount_converted_sell_price) - float(amount_converted_buy_price)

    transactions = Transaction.objects.all()


    data = []
    for tx in transactions:
        if tx.tx_type == 'sell':
            profit = -tx.price
            data.append({'profit': 4, 'symbol': tx.currency_to.symbol, 'name': tx.currency_to.name, 'price': tx.price})

    print(data)
    return render(request,'currencies/profits.html', {'transactions':data})