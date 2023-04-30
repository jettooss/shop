from django.db.models import Sum
from django.shortcuts import render, redirect, get_object_or_404
# from .forms import *
from django.contrib.auth import authenticate, login, logout

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
        'form': product_main.objects.all(),
         'form1':Product_category.objects.all(),
        'form2': Label_Product.objects.all()
     }
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

def show_post(request, post_slug):

    post = get_object_or_404(Label_Product, slug=post_slug)

    products= Product.objects.all().filter(category=post)

    if request.method == 'POST':
        product_id  = request.POST.get('product_name')
        name_product = Product.objects.get(name=product_id )

        messages.info(request, f"Всего выплачено будет:  руб.{name_product.price}")
        saving=Basket(
            user=request.user,

            name=name_product.name,

            price =name_product.price,
        ).save()
    context = {
        "product": products,
    }

    return render(request, 'main/product.html' ,context)

def cabinet(request):

    products= Basket.objects.all().filter(user=request.user)
    total_price = products.aggregate(total=Sum('price'))['total'] or 0

    context = {
        "product": products,
        "total_price":total_price
    }

    return render(request, 'main/personal_account.html',context)


def logoutUser(request):
    logout((request))
    return redirect('main')



def delete_order(request, order_id):
    order = get_object_or_404(Basket, id=order_id)
    order.delete()
    return redirect('cabinet')


def checkout(request):
    user = request.user
    basket_items = Basket.objects.filter(user=user)
    total_price = sum(item.price for item in basket_items)

    order = Order.objects.create(
        user=user,
        total_price=total_price
    )
    for item in basket_items:
        order_item = OrderItem.objects.create(
            order=order,
            name=item.name,
            price=item.price,
            quantity=1
        )
    basket_items.delete()

    return render(request, 'main/checkout.html', {'order': order})