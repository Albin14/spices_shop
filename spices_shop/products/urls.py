from django.urls import path
from django.contrib.staticfiles.urls import static
from django.conf import settings
from products import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('product_list/', views.list_products, name='list_products'),
    path('product_details/<pk>', views.product_detail, name='detail_product'),
    

]
