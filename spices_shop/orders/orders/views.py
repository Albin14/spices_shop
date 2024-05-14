from django.shortcuts import render, redirect
from .models import Order, OrderedItem
from django.contrib import messages
from products.models import Product
from django.contrib.auth.decorators import login_required
# Create your views here.


def show_cart(request): 
    user = request.user
    customer = user.customer_profile
    cart_obj, created = Order.objects.get_or_create(
        owner=customer,
        order_status=Order.CART_STAGE)
    context = {'cart': cart_obj}
    return render(request, 'cart.html', context)


def remove_from_cart(request, pk):
    item = OrderedItem.objects.get(pk=pk)
    if item:
        item.delete()
    return redirect('cart')



def checkout_cart(request):
    if request.POST:
        try:
            user = request.user
            customer = user.customer_profile
            total = float(request.POST.get('total'))
            order_obj = Order.objects.get(
                owner=customer,
                order_status=Order.CART_STAGE
            )
            if order_obj:
                order_obj.order_status = Order.ORDER_CONFIRMED  # Order confirmed
                order_obj.total_price=total
                order_obj.save()
                status_msg = 'Your Order Confirmed Successfully'
                messages.success(request, status_msg)

            else:
                status_msg = 'No items in your cart'
                messages.error(request, status_msg)

        except:
            status_msg = 'Something went wrong'
            messages.error(request, status_msg)
    return redirect('cart')



@login_required(login_url='account')
def add_to_cart(request):
    if request.POST:
        user = request.user
        customer = user.customer_profile
        count = int(request.POST.get('count'))
        product_id = int(request.POST.get('product_id'))
        cart_obj, created = Order.objects.get_or_create(
            owner=customer,
            order_status=Order.CART_STAGE
        )
        product = Product.objects.get(pk=product_id)
        ordered_item, created = OrderedItem.objects.get_or_create(
            product=product,
            owner=cart_obj
        )
        if created:
            ordered_item.count = count
            ordered_item.save()
        else:
            ordered_item.count += count
            ordered_item.save()
        # Redirect to the same page after
    return redirect('cart')


@login_required(login_url='account')
def view_orders(request):
    user = request.user
    customer = user.customer_profile
    
   
    return render(request, 'cart.html')


@login_required(login_url='account')
def show_orders(request):
    user = request.user
    customer = user.customer_profile
    all_orders= Order.objects.filter(owner=customer).exclude(order_status=Order.CART_STAGE)
    context={'orders':all_orders}
   
    return render(request, 'orders.html',context)
