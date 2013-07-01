# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, 'main/dummy.html', {})

def stores(request):
    store_list = Store.objects.all()
    context = {'stores':store_list}
    return render(request, 'main/stores.html', context)
    
