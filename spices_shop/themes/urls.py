from django.urls import path
from django.contrib.staticfiles.urls import static
from django.conf import settings
from themes import views

urlpatterns = [
    path('themes/',views.theme,name='theme'),
 
    
]