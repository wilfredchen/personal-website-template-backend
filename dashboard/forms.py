from django.forms import ModelForm
from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

class UserEditForm(forms.Form, ModelForm):
  name = forms.CharField(
    widget = forms.TextInput(attrs={'placeholder': 'Yoshida'}),
    label = "Full Name",
    required = True
  )
  email2 = forms.EmailField(
    widget = forms.TextInput(attrs={'placeholder': 'hello@gmail.com'}),
    label = "Email",
    required = True
  )
  bio1 = forms.CharField(
    widget = forms.Textarea(attrs={'rows': 3, 'style': 'resize:none', 'placeholder': 'First line of a little bit about you.'}),
    label = "First Description",
    required = True
  )
  bio2 = forms.CharField(
    widget = forms.Textarea(attrs={'rows': 3, 'style': 'resize:none', 'placeholder': 'Second line of a little bit more about you.'}),
    label = "Second Description",
    required = False
  )
  phone = forms.CharField(
    widget = forms.TimeInput(attrs={'placeholder': '+95 78912346'}),
    label = "Phone",
    required = True
  )
  linkedin_url = forms.CharField(
    widget = forms.TextInput(attrs={'placeholder': 'Your Linkedin profile url'}),
    label = "Linkedin URL",
    required = True
  )
  facebook_url = forms.CharField(
    widget = forms.TextInput(attrs={'placeholder': 'Your Facebook profile url'}),
    label = "Facebook URL",
    required = False
  )
  twitter_url = forms.CharField(
    widget = forms.TextInput(attrs={'placeholder': 'Your Twitter profile url'}),
    label = "Twitter URL",
    required = False
  )
  
  class Meta:
    model = User
    fields = ['name', 'email2', 'bio1', 'bio2', 'phone', 'linkedin_url', 'facebook_url', 'twitter_url']
    

  def clean(self):
    cleaned_data = super(UserEditForm, self).clean()
    # name = cleaned_data.get("name")
    # email = cleaned_data.get("email")
    # if len(name) > 250:
    #   self.add_error('name', "Why your name so long")
    return cleaned_data


  

