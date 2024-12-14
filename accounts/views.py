import os
from django.shortcuts import redirect, render, HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import UserRegisterForm, UserLoginForm

# Create your views here.
def registerView(request):
    form = UserRegisterForm()
    context = {
        'form': form,
    }
    if request.method == 'POST':
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save() # Save user to Database
            username = form.cleaned_data.get('username') # Get the username that is submitted
            messages.success(request, f'Account created for {username}!') # Show sucess message when account is created
            return redirect('login') # Redirect user to Homepage
        else:
            return HttpResponse('form not valid')
    else:
        return render(request, 'accounts/register.html', context)


def logoutView(request):
    logout(request)
    return redirect('index')


def loginView(request):
    form = UserLoginForm()
    context = {
        'form': form,
    }
    if request.method == 'POST':
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user != None:
            login(request, user)
            messages.success(request, 'You have logged in successfully')
            return HttpResponse('successfull')
        else:
            context['form'] = UserLoginForm(request.POST)
            messages.error(request, 'Username or password incorrect')
            return render(request, 'accounts/login.html', context)
    else:
        return render(request, 'accounts/login.html', context)