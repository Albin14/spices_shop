from django.urls import path
from shop_owner_app import views

urlpatterns=[
    path('shop_owner/shop_login/',views. shop_owner_login, name='login'),
    path('shop_owner/logout/',views.logout,name='logout'),
    path('shop_owner/register/',views. shop_owner_register, name='register'),
    path('shop_owner/shop_dashboard/', views.dashboard, name='dashboard'),
    path('shop_owner/shop_detail<int:shop_id>/', views.shop_detail, name='shop_detail'),
    path('shop_owner/add_product/', views.add_product, name='add_product'),
    # 

]