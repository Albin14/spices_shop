from django.urls import path
from django.contrib.staticfiles.urls import static
from django.conf import settings
from customers import views

urlpatterns = [
    
    path('customer-login/',views.show_account,name='customer_login'),
    path('logout',views.signout,name='logout'),

    
]