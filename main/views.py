
from django.shortcuts import render, redirect, get_object_or_404
# from .forms import *
# from django.contrib import messages
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth import authenticate, login as dj_login
# from django.contrib.auth.decorators import login_required
# from .models import *

def main(request):
    return render(request, 'main/main.html')