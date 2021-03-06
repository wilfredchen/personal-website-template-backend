from django.contrib.auth import authenticate
from django.db.models.query import Prefetch
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CertificateForm, SkillForm, UserEditForm, PasswordUpdateForm, ProfilePhotoForm, ExperiencesForm, EducationForm, TagForm, PortfolioForm, UpdatePortfolioForm, BlogForm, UpdateBlogForm, CVForm
from .models import Experiences, Education, Certificates, Skills, Tags, Portfolios, UISetting, Blog
import random
from django.db import connection

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
    else:
      messages.error(request, "Email or Password is incorrect!")
      
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
  cvForm = CVForm()
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
    
    if "update_cv" in request.POST:#if form contain update_cv
      cvForm = CVForm(request.POST, request.FILES, instance=user)
      if cvForm.is_valid():
        cvForm.save()
        return redirect('home')
      
  context = {'userEditForm': userEditForm, 'passwordUpdateForm': passwordUpdateForm, 'profilePhotoForm': profilePhotoForm, 'cvForm': cvForm,
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


#Certificate Page
@login_required(login_url = 'login')
def certificatePage(request):
  addCertiForm = CertificateForm()
  certificates = Certificates.objects.all()
  
  if request.method == 'POST':
    if "add_certi" in request.POST:
      addCertiForm = CertificateForm(request.POST)
      if addCertiForm.is_valid():
        addCertiForm.save()
        return redirect('certificates')
    
    if "delete_certi" in request.POST:
      certi = Certificates.objects.get(id=request.POST.get('certiId'))
      certi.delete()
      return redirect('certificates')
  
  context={'addCertiForm': addCertiForm, 'certificates': certificates}
  return render(request, 'dashboard/certi/certificates.html', context)


#Update certificate page
@login_required(login_url = 'login')
def updateCertificatePage(request, pk):
  certificates = Certificates.objects.get(id=pk)
  updateCertiForm = CertificateForm(instance=certificates)
  
  if request.method == 'POST':
    updateCertiForm = CertificateForm(request.POST, instance=certificates)
    if updateCertiForm.is_valid():
      updateCertiForm.save()
      return redirect('certificates')
    
  context={'updateCertiForm': updateCertiForm}
  return render(request, 'dashboard/certi/update_certificates.html', context)


#Skills Page
@login_required(login_url = 'login')
def skillPage(request):
  addSkillForm = SkillForm()
  skills = Skills.objects.all()
  
  if request.method == 'POST':
    if "add_skill" in request.POST:
      addSkillForm = SkillForm(request.POST)
      if addSkillForm.is_valid():
        addSkillForm.save()
        return redirect('skills')
    
    if "delete_skill" in request.POST:
      skills = Skills.objects.get(id=request.POST.get('skillId'))
      skills.delete()
      return redirect('skills')
  
  context={'addSkillForm': addSkillForm, 'skills': skills}
  return render(request, 'dashboard/skills/skills.html', context)


#Update skills page
@login_required(login_url = 'login')
def updateSkillPage(request, pk):
  skills = Skills.objects.get(id=pk)
  updateSkillForm = SkillForm(instance=skills)
  
  if request.method == 'POST':
    updateSkillForm = SkillForm(request.POST, instance=skills)
    if updateSkillForm.is_valid():
      updateSkillForm.save()
      return redirect('skills')
    
  context={'updateSkillForm': updateSkillForm}
  return render(request, 'dashboard/skills/update_skills.html', context)


#Tags Page
@login_required(login_url = 'login')
def tagPage(request):
  addTagForm = TagForm()
  tags = Tags.objects.all()
  
  if request.method == 'POST':
    if "add_tag" in request.POST:
      addTagForm = TagForm(request.POST)
      if addTagForm.is_valid():
        addTagForm.save()
        return redirect('tags')
    
    if "delete_tag" in request.POST:
      tags = Tags.objects.get(id=request.POST.get('tagId'))
      tags.delete()
      return redirect('tags')
  
  context={'addTagForm': addTagForm, 'tags': tags}
  return render(request, 'dashboard/tags/tags.html', context)


#Update tags page
@login_required(login_url = 'login')
def updateTagPage(request, pk):
  tags = Tags.objects.get(id=pk)
  updateTagForm = TagForm(instance=tags)
  
  if request.method == 'POST':
    updateTagForm = TagForm(request.POST, instance=tags)
    if updateTagForm.is_valid():
      updateTagForm.save()
      return redirect('tags')
    
  context={'updateTagForm': updateTagForm}
  return render(request, 'dashboard/tags/update_tags.html', context)


#Portfoio Page
@login_required(login_url = 'login')
def portfolioPage(request):
  addPortfolioForm = PortfolioForm()
  portfolios = Portfolios.objects.all()
  tags = Tags.objects.all()
  
  if request.method == 'POST':
    if "add_portfolio" in request.POST:
      addPortfolioForm = PortfolioForm(request.POST, request.FILES)
      if addPortfolioForm.is_valid():
        newPortfolio = Portfolios.objects.create(
          image_path = request.FILES['image_path'],
          title = request.POST.get('title'),
          short_desc = request.POST.get('short_desc'),
          url = request.POST.get('url'),
        )
        for tag in request.POST.getlist('tag'):
          newPortfolio.tags.add(Tags.objects.get(id=tag))
        
        newPortfolio.save()
        return redirect('portfolios')
    
    if "delete_portfolio" in request.POST:
      portfolios = Portfolios.objects.get(id=request.POST.get('portfolioId'))
      portfolios.tags.clear()
      portfolios.delete()
      return redirect('portfolios')
  
  context={'addPortfolioForm': addPortfolioForm, 'portfolios': portfolios, 'tags': tags, }
  return render(request, 'dashboard/portfolios/portfolios.html', context)


#Update Portfoio page
@login_required(login_url = 'login')
def updatePortfolioPage(request, pk):
  portfolios = Portfolios.objects.get(id=pk)
  updatePortfolioForm = UpdatePortfolioForm(instance=portfolios)
  tags = Tags.objects.all()
  used_tags = portfolios.tags.all()
  if request.method == 'POST':
    updatePortfolioForm = PortfolioForm(request.POST, request.FILES, instance=portfolios)
    if updatePortfolioForm.is_valid():
      portfolios.title = request.POST.get('title')
      portfolios.short_desc = request.POST.get('short_desc')
      portfolios.url = request.POST.get('url')
      if request.FILES:
        portfolios.image_path = request.FILES['image_path']
      if request.POST.getlist('tag'):
        portfolios.tags.clear()
        for tag in request.POST.getlist('tag'):
          portfolios.tags.add(Tags.objects.get(id=tag))
      
      portfolios.save()
      return redirect('portfolios')
    
  context={'updatePortfolioForm': updatePortfolioForm, 'tags': tags, 'used_tags': used_tags}
  return render(request, 'dashboard/portfolios/update_portfolios.html', context)


@login_required(login_url = 'login')
def setting(request):
  uiSetting = UISetting.objects.all()
  if request.method == 'POST':
    if "update_ui_settings" in request.POST:
      uiSettingUpdateAbout = UISetting.objects.get(name='About')
      uiSettingUpdateContact = UISetting.objects.get(name='Contact')
      uiSettingUpdatePortfolios = UISetting.objects.get(name='Portfolios')
      uiSettingUpdateBlog = UISetting.objects.get(name="Blog")
      
      if request.POST.get('About') == 'on':
        uiSettingUpdateAbout.show = True
        uiSettingUpdateAbout.save()
      else:
        uiSettingUpdateAbout.show = False
        uiSettingUpdateAbout.save()
        
      if request.POST.get('Contact') == 'on':
        uiSettingUpdateContact.show = True
        uiSettingUpdateContact.save()
      else:
        uiSettingUpdateContact.show = False
        uiSettingUpdateContact.save()
        
      if request.POST.get('Portfolios') == 'on':
        uiSettingUpdatePortfolios.show = True
        uiSettingUpdatePortfolios.save()
      else:
        uiSettingUpdatePortfolios.show = False
        uiSettingUpdatePortfolios.save()
        
      if request.POST.get('Blog') == 'on':
        uiSettingUpdateBlog.show = True
        uiSettingUpdateBlog.save()
      else:
        uiSettingUpdateBlog.show = False
        uiSettingUpdateBlog.save()
  
  context={'uiSetting':uiSetting}
  return render(request, 'dashboard/setting/setting.html', context)


@login_required(login_url='login')
def blogPage(request):
  blogForm = BlogForm()
  blogs = Blog.objects.all()
  tags = Tags.objects.all()
  if request.method == 'POST':
    if "add_blog" in request.POST:
      blogForm = BlogForm(request.POST, request.FILES)
      if blogForm.is_valid():
        newblog = Blog.objects.create(
          image_path = request.FILES['image_path'],
          title = request.POST.get('title'),
          short_desc = request.POST.get('short_desc'),
          main_desc = request.POST.get('main_desc'),
        )
        for tag in request.POST.getlist('tag'):
          newblog.tags.add(Tags.objects.get(id=tag))
          
        newblog.save()
        return redirect('blog')
      
    if "delete_blog" in request.POST:
      blog = Blog.objects.get(id=request.POST.get('blogId'))
      blog.tags.clear()
      blog.delete()
      return redirect('blog')
   
  context={'blogForm': blogForm, 'blogs': blogs, 'tags': tags}
  return render(request, 'dashboard/blog/blog.html', context)


#Update blog page
@login_required(login_url = 'login')
def updateBlogPage(request, pk):
  blog = Blog.objects.get(id=pk)
  print(connection.queries)
  blogForm = UpdateBlogForm(instance=blog)
  tags = Tags.objects.all()
  used_tags = blog.tags.all()
  
  if request.method == 'POST':
    blogForm = BlogForm(request.POST, request.FILES, instance=blog)
    if blogForm.is_valid():
      blog.title = request.POST.get('title')
      blog.short_desc = request.POST.get('short_desc')
      blog.main_desc = request.POST.get('main_desc')
      if request.FILES:
        blog.image_path = request.FILES['image_path']
      if request.POST.getlist('tag'):
        blog.tags.clear()
        for tag in request.POST.getlist('tag'):
          blog.tags.add(Tags.objects.get(id=tag))
      blog.save()
      return redirect('blog')
  context={'blogForm': blogForm, 'tags': tags, 'used_tags': used_tags }        
  return render(request, 'dashboard/blog/update_blog.html', context)