# Create your views here.
from django.shortcuts import render

from models import Store

from django import forms

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django import forms


class UserRegistrationForm(forms.Form):
  username = forms.CharField(label=u'Username')
  password = forms.CharField(label=u'Password', widget=forms.PasswordInput())
  ##confirmPS = forms.CharField(label=u'Confirm Password', widget=forms.PasswordInput())
  email = forms.CharField(label=u'Email')
  first_name = forms.CharField(label=u'First Name')
  last_name = forms.CharField(label=u'Last Name')

# Create your views here.
def showlogin(request):
  return render(request, 'main/submit/login.html', {'form': UserRegistrationForm()})

def submitlogin(request):
  Username = request.POST['username']
  Password = request.POST['password']
  user = authenticate(username=Username, password=Password)
  if user is not None:
    if user.is_active:
      login(request, user)
      return HttpResponseRedirect('profile')
  return HttpResponseRedirect('login')

@login_required
def profile(request):
  context = {'username': request.user.username}
  return render(request, 'main/submit/profile.html', context)

#def log_me_out(request):
#  logout(request)
#  return HttpResponseRedirect('/home')

def register(request):
  if request.method == 'POST':
    form = UserRegistrationForm(request.POST)
    if form.is_valid(): ##and form.cleaned_data['password'] == form.cleaned_data['confirmPS']:
      User.objects.create_user(form.cleaned_data['username'],
                               form.cleaned_data['email'],
                               form.cleaned_data['password'],
                  first_name=form.cleaned_data['first_name'],
                  last_name=form.cleaned_data['last_name'],)
      user = authenticate(username=form.cleaned_data['username'],
                          password=form.cleaned_data['password'])
      login(request, user)
      return HttpResponseRedirect('profile')
    else:
      return HttpResponseRedirect('media')
  form = UserRegistrationForm()
  return render(request, 'main/submit/register.html', {'form': form})

###################################


def first(request):
    return render(request, 'main/first.html', {})

def home(request):
    return render(request, 'main/dummy.html', {})


def stores(request):
    store_list = Store.objects.all()
    context = {'stores':store_list}
    return render(request, 'main/stores.html', context)

def maps(request):
	return render(request, 'main/maps.html', {})

def holy(request):
	return render(request, 'main/holy.html', {})

def introduction(request):
	return render(request, 'main/introduction.html', {})

def media(request):
	return render(request, 'main/media.html', {})
###########################################

@login_required
def submitBusiness(request):
	return render(request, 'main/submitBusiness.html', {})

def submitBusiness_accepted(request):
	Name = request.POST['name']
	Owner = request.user
	StoreType = request.POST['storeType']
	Address = request.POST['address']
	Info = request.POST['info']
	new_store = Store(name = Name, owner = Owner, storeType = StoreType, address = Address, info = Info)
	new_store.save()
	return HttpResponseRedirect('success')

def success(request):
	return render(request, 'main/success.html', {})

###################################################

def about(request):
	return render(request, 'main/about.html', {})

def contact(request):
	return render(request, 'main/contact.html', {})
