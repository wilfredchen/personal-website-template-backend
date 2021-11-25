from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserEditForm, PasswordUpdateForm, ProfilePhotoForm, AddExperiencesForm
from .models import Experiences
import random
# Create your views here.

#login model
def loginPage(request):
  if request.user.is_authenticated:
    return redirect('home')
  if request.method == 'POST':
    email = request.POST.get('email').lower()
    password = request.POST.get('password') 
    
    user = authenticate(request, email = email, password = password)
    if user is not None:
      login(request,user)
      return redirect('home')
      
  context = {}
  return render(request, 'dashboard/login.html', context)


#logout model
def logOutUser(request):
  logout(request)
  return redirect('home')


#home page model
@login_required(login_url = 'login')
def homePage(request):
  user = request.user
  userEditForm = UserEditForm(instance=user)
  passwordUpdateForm = PasswordUpdateForm()
  profilePhotoForm = ProfilePhotoForm()
  randNum = random.randint(1, 5)
  defaultImg = f'images/profile{randNum}.jpg'
  
  if request.method == 'POST':
    if "update_user_info" in request.POST: #if form contain update_user_info
      userEditForm = UserEditForm(request.POST, instance=user)
      if userEditForm.is_valid(): #if form is valid
        userEditForm.save()
        return redirect('home')
    
    if "update_user_password" in request.POST:#if form contain update_user_password
      passwordUpdateForm = PasswordUpdateForm(request.POST, instance=user) 
      if passwordUpdateForm.is_valid(): #if form is valid
        if user.check_password(request.POST.get('current_password')): #check current password is valid, if valid update password
          user.set_password(request.POST.get('password'))
          user.save()
          messages.success(request, "Password updated")
        else:
          messages.error(request, "Please provide a valid current password")
        
    if "update_profile_photo" in request.POST:#if form contain update_profile_photo
      profilePhotoForm = ProfilePhotoForm(request.POST, request.FILES, instance=user)
      if profilePhotoForm.is_valid(): #if form is valid
        profilePhotoForm.save() #update profile photo, django clean up auto delete the old photo file from media
        return redirect('home')
      
  context = {'userEditForm': userEditForm, 'passwordUpdateForm': passwordUpdateForm, 'profilePhotoForm': profilePhotoForm, 
             'profile_photo': user.profile_photo, 'defaultImg': defaultImg}
  return render(request, 'dashboard/index/index.html', context)


#experiences page model
@login_required(login_url = 'login')
def experiencesPage(request):
  addExpForm = AddExperiencesForm()
  experiences = Experiences.objects.all()
  
  if request.method == 'POST':
    if "add_exp" in request.POST:
      addExpForm = AddExperiencesForm(request.POST)
      if addExpForm.is_valid():
        addExpForm.save()
        return redirect('experiences')
  
    if "delete_exp" in request.POST:
      exp = Experiences.objects.get(id=request.POST.get('expId'))
      exp.delete()
      return redirect('experiences')
  
  context={'addExpForm': addExpForm, 'experiences': experiences}
  return render(request, 'dashboard/experiences.html', context)
