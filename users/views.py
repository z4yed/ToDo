from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.db import IntegrityError

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
                messages.success(request, "Account Created Successfully. ")
                return redirect('home-view')
            except IntegrityError:
                messages.error(request, "Username already Taken. Choose a new one. ")
                return render(request, 'users/signup.html', context)
    return render(request, 'users/signup.html', context)
