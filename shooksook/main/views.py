# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, 'main/dummy.html', {})

def stores(request):
    return render(request, 'main/stores.html', {})
    
