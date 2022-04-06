from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import AuthForm, RegisterForm
from datetime import datetime
from django.contrib.auth import logout
from .models import Profile


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


def register(request):
    if request.method=='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            city =form.cleaned_data.get('city')
            phone_number=form.cleaned_data.get('phone_number')
            Profile.objects.create(
                user=user,
                city=city,
                phone_number=phone_number,
            )
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})


def account(request):
    return render(request, 'users/account.html')
