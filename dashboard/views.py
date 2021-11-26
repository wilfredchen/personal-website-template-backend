from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserEditForm, PasswordUpdateForm, ProfilePhotoForm, ExperiencesForm, EducationForm
from .models import Experiences, Education
import random
# Create your views here.

#login
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


#logout
def logOutUser(request):
  logout(request)
  return redirect('home')


#home page
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


#Experiences page
@login_required(login_url = 'login')
def experiencesPage(request):
  addExpForm = ExperiencesForm()
  experiences = Experiences.objects.all()
  
  if request.method == 'POST':
    if "add_exp" in request.POST:
      addExpForm = ExperiencesForm(request.POST)
      if addExpForm.is_valid():
        addExpForm.save()
        return redirect('experiences')
  
    if "delete_exp" in request.POST:
      exp = Experiences.objects.get(id=request.POST.get('expId'))
      exp.delete()
      return redirect('experiences')
  
  context={'addExpForm': addExpForm, 'experiences': experiences}
  return render(request, 'dashboard/experiences/experiences.html', context)


#Update experience page
@login_required(login_url = 'login')
def updateExperiencesPage(request, pk):
  experiences = Experiences.objects.get(id=pk)
  updateExpForm = ExperiencesForm(instance=experiences)
  
  if request.method == 'POST':
    updateExpForm = ExperiencesForm(request.POST, instance=experiences)
    if updateExpForm.is_valid():
      updateExpForm.save()
      return redirect('experiences')
  
  context={'updateExpForm': updateExpForm}
  return render(request, 'dashboard/experiences/update_experiences.html', context)


#Education page
@login_required(login_url = 'login')
def educationsPage(request):
  addEduForm = EducationForm()
  educations = Education.objects.all()
  
  if request.method == 'POST':
    if "add_edu" in request.POST:
      addEduForm = EducationForm(request.POST)
      if addEduForm.is_valid():
        addEduForm.save()
        return redirect('educations')
    
    if "delete_edu" in request.POST:
      edu = Education.objects.get(id=request.POST.get('eduId'))
      edu.delete()
      return redirect('educations')
    
  context={'addEduForm': addEduForm, 'educations': educations}
  return render(request, 'dashboard/educations/educations.html', context)


#Update educations page
@login_required(login_url = 'login')
def updateEducationsPage(request, pk):
  educations = Education.objects.get(id=pk)
  updateEduForm = EducationForm(instance=educations)
  
  if request.method == 'POST':
    updateEduForm = EducationForm(request.POST, instance=educations)
    if updateEduForm.is_valid():
      updateEduForm.save()
      return redirect('educations')
  
  context={'updateEduForm':updateEduForm}
  return render(request, 'dashboard/educations/update_educations.html', context)