from django.forms import ModelForm
from .models import User
from django.contrib.auth.forms import UserCreationForm

class UserEditForm(UserCreationForm):
  class Meta:
    model = User
    fields = ['name', 'email2', 'bio1', 'bio2', 'phone', 'linkedin_url', 'facebook_url', 'twitter_url']