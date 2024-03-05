from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login,logout as auth_logout, authenticate
from accounts.forms import RegisterForm, LoginForm
from django.urls import reverse

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            if user.user_type == 'customer' or user.user_type == 'owner':
                return redirect(reverse('login'))
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

  
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('home')
            else:
                form.add_error(None,'ชื่อผู้ใช้หรือรหัสผ่านผิดพลาด กรุณาลองอีกครั้ง') 
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})


def logout(request):
    auth_logout(request)
    return redirect('home')