from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit
# Create your models here.

class User(AbstractUser):
  name = models.CharField(max_length=250, null=True)
  email = models.EmailField(unique=True, null=True)
  email2 = models.EmailField(unique=True, null=True)
  bio1 = models.TextField(null=True)
  bio2 = models.TextField(null=True)
  profile_photo = ProcessedImageField(processors=[ResizeToFit(600)],format='JPEG',options={'quality': 70},null = True)
  phone = models.CharField(max_length=200, null=True)
  linkedin_url = models.TextField(null=True)
  facebook_url = models.TextField(null=True)
  twitter_url = models.TextField(null=True)
  
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = []


class Experiences(models.Model):
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now = True)
  year = models.CharField(max_length=250, null=False)
  title = models.CharField(max_length=250, null=False)
  company = models.CharField(max_length=250, null=False)
  short_desc = models.TextField(null=True)
  
  class Meta:
    ordering = ['-created_at']

  def __str__(self):
    return self.short_desc[0:250] #return first 250 word characters only for short desc.


class Education(models.Model):
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now = True)
  year = models.CharField(max_length=250, null=False)
  major = models.CharField(max_length=250, null=False)
  school = models.CharField(max_length=250, null=False)
  grade = models.CharField(max_length=250, null=False)
  
  class Meta:
    ordering = ['-created_at']
  