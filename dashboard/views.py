from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserEditForm
# Create your views here.

def loginPage(request):
  if request.user.is_authenticated:
    return redirect('home')
  if request.method == 'POST':
    email = request.POST.get('email').lower()
    password = request.POST.get('password') 
    
    user = authenticate(request, email = email, password = password)
    print(user)
    if user is not None:
      print("user is not none")
      login(request,user)
      return redirect('home')
      
  context = {}
  return render(request, 'dashboard/login.html', context)


@login_required(login_url = 'login')
def homePage(request):
  userEditForm = UserEditForm()
  context = {'userEditForm': userEditForm}
  return render(request, 'dashboard/index.html', context)



