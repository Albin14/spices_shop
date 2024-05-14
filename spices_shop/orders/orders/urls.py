from django.urls import path
from django.contrib.staticfiles.urls import static
from django.conf import settings
from . import views

urlpatterns = [
    path('cart/', views.show_cart, name='cart'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('remove_item/<int:pk>/', views.remove_from_cart, name='remove_item'),
    path('checkout/', views.checkout_cart, name='checkout'),
    path('orders/', views.show_orders, name='orders'),
    # payment
    #     path('payment/',views.payment,name='payment'),
    #     path('payment_success/',views.payment_success,name='payment_success'),
    #     path('payment_failure/',views.payment_failure,name='payment_failure'),
    #     path('payment_cancelled/',views.payment_cancelled,name='payment_cancelled'),

]
