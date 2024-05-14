from django.urls import path
from .import views

urlpatterns=[
    path('login/',views.admin_login, name='admin_login'),
    path('dashboard/',views.admin_dashboard, name='admin_dashboard'),
    path('logout/',views.logout,name='logout'),
    path('shop_approval_list/', views.shop_approval_list, name='admin_approval'),
    path('admin1/approve_shop/<int:shop_id>/', views.approve_shop, name='approve_shop'),
    path('admin1/reject_shop/<int:shop_id>/', views.reject_shop, name='reject_shop'),
    path('view_shop_owners/', views.view_shop_owners, name='view_shop_owners'),
    path('view_customers/', views.view_customers, name='view_customers'),
   
]