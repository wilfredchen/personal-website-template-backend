from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
  name = models.CharField(max_length=250, null=True)
  email = models.EmailField(unique=True, null=True)
  email2 = models.EmailField(unique=True, null=True)
  bio1 = models.TextField(null=True)
  bio2 = models.TextField(null=True)
  profile_photo = models.ImageField(null=True)
  phone = models.CharField(max_length=200, null=True)
  linkedin_url = models.TextField(null=True)
  facebook_url = models.TextField(null=True)
  twitter_url = models.TextField(null=True)
  
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = []

  
  