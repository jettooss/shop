
from django.shortcuts import render, redirect, get_object_or_404
# from .forms import *
# from django.contrib import messages
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth import authenticate, login as dj_login
# from django.contrib.auth.decorators import login_required
# from .models import *
from django.core.files.storage import  FileSystemStorage
from .forms import *
from django.contrib import messages
def main(request):

    context = {
        'form': product_main.objects.all()}
    return render(request, 'main/main.html',context)


def create(request):


    if request.method == 'POST':
        u_form = Main_form(request.POST, request.FILES)
        # product = request.POST.get('product')
        # messages.info(request, f'{product}')
        if u_form.is_valid():
            product = request.POST.get('product')
            messages.info(request, f'вы ввели неверные данные')
            сard_number = request.POST.get('card_number')
            u_form.save()
    #
    else:
          u_form = Main_form


    return render(request, 'main/create.html', {'u_form':u_form})
