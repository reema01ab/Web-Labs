
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'You have successfully registered')
            return redirect('listbooks_part1')
        else:
            messages.error(request, 'Registration error')
    else:
        form = UserCreationForm()

    return render(request, 'usermodule/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Login successfully')
            return redirect('listbooks_part1')
        else:
            messages.error(request, 'Login error')
    else:
        form = AuthenticationForm()

    return render(request, 'usermodule/login.html', {'form': form})


def user_logout(request):
    logout(request)
    messages.success(request, 'Logout successfully')
    return redirect('users.login')

