from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required

# Create your views here.


def user_signup(request):
    context = {
        'form': UserCreationForm()
    }

    if request.method == "POST":
        if request.POST['password1'] != request.POST['password2']:
             messages.error(request, "Password didn't match. ")
             return render(request, 'users/signup.html', context)
        else:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                messages.success(request, "Account Created Successfully. You Can Now Login. ")
                return redirect('user-login')
            except IntegrityError:
                messages.info(request, "Username already Taken. Choose a new one. ")
                return render(request, 'users/signup.html', context)
    return render(request, 'users/signup.html', context)


def user_login(request):
    context = {
        'form' : AuthenticationForm()
    }
    if request.method == "POST":
        user = authenticate(request, username = request.POST['username'], password= request.POST['password'])
        if user is not None:
            auth_login(request, user)
            messages.success(request, "Login Successull.")
            return redirect('home-view')
        else:
            messages.info(request, 'Wrong Credential. Try Again. ')
            return render(request, 'users/login.html', context)
    return render(request, 'users/login.html', context)

@login_required
def user_logout(request):
    if request.method == "POST":
        auth_logout(request)
        messages.info(request, "Logout Succesfull.")
        return redirect('home-view')
