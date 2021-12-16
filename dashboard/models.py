from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit
from tinymce import models as tinymce_models
# Create your models here.

class User(AbstractUser):
  name = models.CharField(max_length=250, null=True)
  email = models.EmailField(unique=True, null=True)
  email2 = models.EmailField(unique=True, null=True)
  role = models.CharField(max_length=250, null=True)
  bio1 = models.TextField(null=True)
  bio2 = models.TextField(null=True)
  age = models.IntegerField(null=True)
  nationality = models.CharField(max_length=200,null = True)
  profile_photo = ProcessedImageField(upload_to='images', processors=[ResizeToFit(1650)],format='JPEG',options={'quality': 75},null = True)
  phone = models.CharField(max_length=200, null=True)
  linkedin_url = models.TextField(null=True)
  facebook_url = models.TextField(null=True)
  twitter_url = models.TextField(null=True)
  languages = models.CharField(max_length=250, null = True)
  current_resident = models.CharField(max_length=250, null = True)
  cv_path = models.FileField(upload_to='documents', null=True)
  
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['username']


class Experiences(models.Model):
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now = True)
  year = models.CharField(max_length=250, null=False)
  title = models.CharField(max_length=250, null=False)
  company = models.CharField(max_length=250, null=False)
  short_desc = models.TextField(null=True)
  location = models.CharField(max_length=250, null=True)
  
  class Meta:
    ordering = ['-created_at']

  def __str__(self):
    return self.short_desc[0:300] #return first 300 word characters only for short desc.


class Education(models.Model):
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now = True)
  year = models.CharField(max_length=250, null=False)
  major = models.CharField(max_length=250, null=False)
  school = models.CharField(max_length=250, null=False)
  grade = models.CharField(max_length=250, null=False)
  location = models.CharField(max_length=250, null=True)
  
  class Meta:
    ordering = ['-created_at']


class Certificates(models.Model):
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now = True)
  year = models.CharField(max_length=250, null=False)
  title = models.CharField(max_length=250, null=False)
  award_body = models.CharField(max_length=250, null=False)
  url = models.TextField(null=True)
  
  class Meta:
    ordering = ['-created_at']


class Skills(models.Model):
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now = True)
  name = models.CharField(max_length=250, null = False)
  percentage = models.IntegerField(null = False)
  
  class Meta:
    ordering = ['-created_at']
    

class Tags(models.Model):
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now = True)
  name = models.CharField(max_length=250, null=False, unique=True)
  
  class Meta:
    ordering = ['-created_at']
    

class Portfolios(models.Model):
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now = True)
  image_path = ProcessedImageField(upload_to='images', processors=[ResizeToFit(500)],format='JPEG',options={'quality': 70},null = True)
  title = models.CharField(max_length=250, null=False)
  short_desc = models.TextField(null=False)
  url = models.TextField(null=True)
  tags = models.ManyToManyField(Tags, blank=True, related_name="tags")
  
  class Meta:
    ordering = ['-created_at']


class UISetting(models.Model):
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now = True)
  name = models.CharField(max_length=250, null = False, unique = True)
  show = models.BooleanField()
  
  class Meta:
    ordering = ['name']
    

class Blog(models.Model):
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now = True)
  image_path = ProcessedImageField(upload_to='images', processors=[ResizeToFit(600)],format='JPEG',options={'quality': 70},null = True)
  title = models.CharField(max_length=250, null = False)
  short_desc = models.TextField(null=False)
  main_desc = tinymce_models.HTMLField()
  tags = models.ManyToManyField(Tags, blank=True)
  
  class Meta:
    ordering = ['-created_at']
