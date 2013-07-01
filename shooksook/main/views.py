# Create your views here.
from django.shortcuts import render
from models import Store

def home(request):
    return render(request, 'main/dummy.html', {})

def stores(request):
    store_list = Store.objects.all()
    context = {'stores':store_list}
    return render(request, 'main/stores.html', context)

def maps(request):
	return render(request, 'main/maps.html', {})

def restaurants(request):
	return render(request, 'main/restaurants.html', {})

def introduction(request):
	return render(request, 'main/introduction.html', {})

def media(request):
	return render(request, 'main/media.html', {})

def submit(request):
	return render(request, 'main/submit.html', {})

def about(requset):
	return render(request, 'main/about.html', {})

def contact(request):
	return render(request, 'main/submit.html', {})
