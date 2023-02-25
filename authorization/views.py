
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import authenticate, login as dj_login
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
def register(request):
    form = CreationForm()

    if request.method == 'POST':
        form = CreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, f'вы зарегистрированы{user}')
            return redirect('login')

    context = {'form': form}
    return render(request, 'authorization/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')

        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            dj_login(request, user)
            return redirect('bank')
        else:
            messages.info(request, f'что не так,{user}')

    return render(request, 'authorization/login.html')
