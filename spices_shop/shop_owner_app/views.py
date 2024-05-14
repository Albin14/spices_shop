# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from .models import ShopOwner,Shop, Product



def shop_owner_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirect to shop owner dashboard
        else:
            messages.info(request,'Invalid username or password')
            return redirect('login')
    else:
        return render(request,'shop_owner/login.html')

def logout(request):
    logout(request)
    return redirect('home')

def shop_owner_register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')
        shop_name = request.POST.get('shop_name')
        shop_address = request.POST.get('shop_address')

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email)
                shop = Shop.objects.create(name=shop_name, address=shop_address, owner=user.username)
                login(request, user)
                messages.success(request, 'Account created successfully and shop created!')
                return redirect('dashboard')
        else:
            messages.error(request, "Passwords didn't match")
    
    return render(request, 'registration/register.html')

@login_required
def dashboard(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        owner = request.user.username

        # Create the shop
        shop = Shop.objects.create(name=name, address=address, owner=owner)
        return HttpResponse({'success': True})

    return render(request, 'shop_owner/dashboard.html')   
@login_required
def create_shop(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        owner = request.user.username

        # Check if the shop name already exists
        if Shop.objects.filter(name=name).exists():
            messages.error(request, 'Shop with this name already exists.')
            return redirect('dashboard')

        # Create the shop
        shop = Shop.objects.create(name=name, address=address, owner=owner)
        messages.success(request, 'Shop created successfully!')
        return redirect('dashboard')

    return render(request, 'shop_owner/create_shop.html')
@login_required
def shop_detail(request, shop_id):
    shop = Shop.objects.get(id=shop_id)
    return render(request, 'shop_owner/shop_detail.html', {'shop': shop})


@login_required
def add_product(request, shop_id):
    shop = Shop.objects.get(id=shop_id)
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        Product.objects.create(name=name, description=description, price=price, shop=shop)
        return redirect('shop:shop_detail', shop_id=shop.id)
    return render(request, 'shop_owner/add_product.html', {'shop': shop})
