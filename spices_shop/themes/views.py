from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
# Create your views here.


def theme(request):
    return render(request, 'themes.html')
