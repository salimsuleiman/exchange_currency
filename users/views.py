from django.shortcuts import render, redirect
from users.models import User
from .forms import EmployeeForm
from django.db import IntegrityError
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

@login_required
def Users(request):
    users = User.objects.filter(is_admin=False)
    # list of users
    # employee
    
    return render(request, 'users/users.html', {'employees': users})

@login_required
def delete(request, ID):
    user = User.objects.filter(id=ID).first()
    if request.method == "POST":
        if user is None:
             return redirect('/users/')
        else:
             user.delete()
             return redirect('/users/')

   
    return render(request, 'users/delete.html', {'user': user})


@login_required
def edit(request, ID):

    user = User.objects.filter(id=ID).first()

    if user is None:
        redirect('/users/')

    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        pass_entry = request.POST['pass_entry']

        try:
            if '' in (first_name, last_name, pass_entry, username):
                messages.add_message(request, messages.INFO, 'الرجاء إدخال كافة الحقول')
                return redirect(f'/users/edit/{ID}/')
            user.first_name = first_name
            user.last_name = last_name
            user.username = username
            user.pass_entry = pass_entry
            user.save()
            return redirect('/users/')
        except IntegrityError:
            messages.add_message(request, messages.INFO, 'الاسم مستخدم من قبل')
            return redirect('/users/')
   
   
    return render(request, 'users/edit.html', {'user': user})

@login_required
def profile(request):
    return render(request, 'users/profile.html')
@login_required
def add(request):
   
   first_name = request.POST['first_name']
   last_name = request.POST['last_name']
   username = request.POST['username']
   pass_entry = request.POST['pass_entry']

   try:
        if '' in (first_name, last_name, pass_entry, username):
            messages.add_message(request, messages.INFO, 'الرجاء إدخال كافة الحقول')
            return redirect('/users/')
        new = User.objects.create(first_name=first_name, last_name=last_name, username=username, pass_entry=pass_entry)
        new.set_password(new.pass_entry)
        new.save()
        print(new)
   except IntegrityError:
        messages.add_message(request, messages.INFO, 'الاسم مستخدم من قبل')
        return redirect('/users/')
   print(new)
   return redirect('/users/')


from django.contrib.auth import logout

def Logout(request):
    logout(request)
    return redirect('/')


def login_page(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
                print('wrong infio1')
                login(request, user)
                return redirect('/')
        else:
            print('wrong infio')
            messages.add_message(request, messages.INFO, 'بيانات تسجيل دخول خاطئة')
            return redirect('/users/login/')

    if request.user.is_authenticated:
        return redirect('/users/')
    else:
        return render(request, 'users/login.html')