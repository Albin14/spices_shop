from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import auth,messages
from shop_owner_app.models import Shop,ShopOwner
from customers.models import Customer
from django.contrib.auth.decorators import login_required
# from .models import ShopOwnerRequest, ShopOwner, Customer



def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Your custom authentication logic
        if username == 'siteadmin' and password == 'siteadmin@123':
            request.session['admin_logged_in'] = True
            return redirect('admin_dashboard')
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'admin/login.html')

def admin_dashboard(request):
    if not request.session.get('admin_logged_in'):
        return redirect('admin_login')
    # Your admin dashboard logic
    return render(request, 'admin/dashboard.html')

def shop_approval_list(request):
    # Get all unapproved shops
    unapproved_shops = Shop.objects.filter(approved=False)
    context = {
        'unapproved_shops': unapproved_shops
    }
    return render(request, 'admin/shop_approval_list.html', context)

def approve_shop(request, shop_id):
    shop = Shop.objects.get(pk=shop_id)
    shop.approved = True
    shop.save()
    return redirect('shop_approval_list')

def reject_shop(request, shop_id):
    shop = Shop.objects.get(pk=shop_id)
    shop.delete()
    return redirect('shop_approval_list')


@login_required
def view_shop_owners(request):
    # Retrieve all shop owners
    shop_owners = ShopOwner.objects.all()
    return render(request, 'admin_app/view_shop_owners.html', {'shop_owners': shop_owners})

@login_required
def view_customers(request):
    # Retrieve all customers
    customers = Customer.objects.all()
    return render(request, 'admin_app/view_customers.html', {'customers': customers})

    
def logout(request):
    logout(request)
    return redirect('home')