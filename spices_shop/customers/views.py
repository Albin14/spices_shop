from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Customer

def signout(request):
    logout(request)
    return redirect("home")

def show_account(request):
    context = {}
    if request.POST and 'register' in request.POST:
        context['register'] = True
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')
            address = request.POST.get('address')
            phone = request.POST.get('phone')

            # Create user accounts
            user = User.objects.create_user(
                username=username,
                password=password,
                email=email
            )
            # Create customer account
            customer = Customer.objects.create(
                name=username,  
                user=user,  
                address=address,
                phone=phone
            )
            success_msg = "User created successfully."
            messages.success(request, success_msg)

        except Exception as e:
            error_msg = "User already exists!!!"
            messages.error(request, error_msg)

    if request.POST and 'login' in request.POST:
        context['login'] = True
        
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user :
            # Check if the user belongs to the 'Customers' group
            login(request, user)
            return redirect("home")
        else:
            error_msg = "Invalid credentials"
            messages.error(request, error_msg)

    return render(request, 'account.html', context)