from django.forms import ModelForm
from django import forms
from .models import Certificates, Experiences, Skills, User, Education, Tags, Portfolios
from django.core.validators import FileExtensionValidator, validate_image_file_extension

# General User Info Form
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
    return cleaned_data


# Password Update Form
class PasswordUpdateForm(forms.Form, ModelForm):
  current_password = forms.CharField(
    widget = forms.PasswordInput(attrs={'placeholder': 'Current Password'}),
    label = "Current Password",
    required = True
  )
  password = forms.CharField(
    widget = forms.PasswordInput(attrs={'placeholder': 'New Password'}),
    label = "New Password",
    required = True
  )
  confirm_password = forms.CharField(
    widget = forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}),
    label = "Confirm Password",
    required = True
  )

  class Meta:
    model = User
    fields = ['password']
  
  field_order = ['current_password', 'password', 'confirm_password']  
  
  def clean(self):
    cleaned_data = super(PasswordUpdateForm, self).clean()
    password = cleaned_data.get("password")
    confirm_password = cleaned_data.get("confirm_password")
    if password is not None and len(password) < 6:
      self.add_error("password", "Password cannot be less than 6 character.")
    if password != confirm_password:
      self.add_error("confirm_password", "Password and confirm password cannot be different.")
    return cleaned_data
  
  
# Profile Photo Update
class ProfilePhotoForm(forms.Form, ModelForm):
  profile_photo = forms.ImageField(
    validators= [validate_image_file_extension, FileExtensionValidator(allowed_extensions=['jpg','jpeg','png'], 
                                                                       message="The image must be in jpg, jpeg or png format.")],
    widget = forms.FileInput(),
    label = "Profile Photo",
    required = True
  )
  
  class Meta:
    model = User
    fields = ['profile_photo']
 
    
# Add/Update Experiences Form
class ExperiencesForm(forms.Form, ModelForm):
  year = forms.CharField(
    widget = forms.TextInput(attrs={'placeholder': '2019 - 2021'}),
    label = "Year",
    required = True
  )
  title = forms.CharField(
    widget = forms.TextInput(attrs={'placeholder': 'Software Engineer'}),
    label = "Job Title",
    required = True
  )
  company = forms.CharField(
    widget = forms.TextInput(attrs={'placeholder': 'Google'}),
    label = "Company Name",
    required = True
  )
  short_desc = forms.CharField(
    widget = forms.Textarea(attrs={'rows': 3, 'style': 'resize:none', 'placeholder': 'A very short description about what you do at your job'}),
    label = "Short Description",
    help_text = "Limited to 300 characters",
    required = False
  )
  
  class Meta:
    model = Experiences
    fields = ['year', 'title', 'company', 'short_desc']
  
  def clean(self):
    cleaned_data = super(ExperiencesForm, self).clean()
    short_desc = cleaned_data.get("short_desc")
    if short_desc is not None and len(short_desc) > 300:
      self.add_error("short_desc", "Your short description is turning into an essay.")
    return cleaned_data


# Add/Update Education Form
class EducationForm(forms.Form, ModelForm):
  year = forms.CharField(
    widget = forms.TextInput(attrs={'placeholder': '2019 - 2021'}),
    label = "Year",
    required = True
  )
  major = forms.CharField(
    widget = forms.TextInput(attrs={'placeholder': 'BSc (Hons) Computing'}),
    label = "Major",
    required = True
  )
  school = forms.CharField(
    widget = forms.TextInput(attrs={'placeholder': 'Oxford University'}),
    label = "School/University",
    required = True
  )
  grade = forms.CharField(
    widget = forms.TextInput(attrs={'placeholder': 'First Class Honor'}),
    label = "Grade",
    required = True
  )
  
  class Meta:
    model = Education
    fields=['year', 'major', 'school', 'grade']


#Add/Update Certificate Form
class CertificateForm(forms.Form, ModelForm):
  year = forms.CharField(
    widget = forms.TextInput(attrs={'placeholder': '2019 - 2021'}),
    label = "Year",
    required = True
  )
  title = forms.CharField(
    widget = forms.TextInput(attrs={'placeholder': 'Python for machine learning'}),
    label = "Certificate Name",
    required = True
  )
  award_body = forms.CharField(
    widget = forms.TextInput(attrs={'placeholder': 'Udemy'}),
    label = "Awarding Body",
    required = True
  )
  url = forms.CharField(
    widget = forms.TextInput(attrs={'placeholder': 'link to your certificate online'}),
    label = "Url",
    required = False
  )
  
  class Meta:
    model = Certificates
    fields = ['year', 'title', 'award_body', 'url']


#Add/Update Skill Form
class SkillForm(forms.Form, ModelForm):
  name = forms.CharField(
    widget = forms.TextInput(attrs={'placeholder': 'Javascript'}),
    label = "Name",
    required = True
  )
  percentage = forms.IntegerField(
    widget = forms.NumberInput(attrs={'placeholder': '80'}),
    label = "Percentage",
    required = True
  )

  class Meta:
    model = Skills
    fields = ['name', 'percentage']


#Add/Update Tags
class TagForm(forms.Form, ModelForm):
  name = forms.CharField(
    widget = forms.TextInput(attrs={'placeholder': 'Web Development'}),
    label = "Name",
    required = True
  )
  
  class Meta:
    model = Tags
    fields = ['name']
    

#Add Portfolio
class PortfolioForm(forms.Form, ModelForm):
  image_path = forms.ImageField(
    validators= [validate_image_file_extension, FileExtensionValidator(allowed_extensions=['jpg','jpeg','png'], 
                                                                       message="The image must be in jpg, jpeg or png format.")],
    widget = forms.FileInput(),
    label = "Portfolio Photo",
    required = True
  )
  title = forms.CharField(
    widget = forms.TextInput(attrs={'placeholder': 'Android Application Development For ABC.org'}),
    label = "Title",
    required = True
  )
  short_desc = forms.CharField(
    widget = forms.Textarea(attrs={'rows': 3, 'style': 'resize:none', 'placeholder': 'A very short description about your portfolio'}),
    label = "Short Description",
    help_text = "Limited to 250 characters",
    required = True
  )
  url = forms.CharField(
    widget = forms.TextInput(attrs={'placeholder': 'Link to your work if any'}),
    label = "Portfolio URL",
    required = False
  )
  tag = forms.MultipleChoiceField(
    choices=Tags.objects.values_list('id', 'name'),
    label="Tags (Multi-choice)",
    required=True,
  )
  
  class Meta:
    model = Portfolios
    fields = ['image_path', 'title', 'short_desc', 'url', 'tag']
  
  def clean(self):
    cleaned_data = super(PortfolioForm, self).clean()
    short_desc = cleaned_data.get("short_desc")
    if short_desc is not None and len(short_desc) > 250:
      self.add_error("short_desc", "Your short description is turning into an essay.")
    return cleaned_data


#Update Portfolio
class UpdatePortfolioForm(forms.Form, ModelForm):
  image_path = forms.ImageField(
    validators= [validate_image_file_extension, FileExtensionValidator(allowed_extensions=['jpg','jpeg','png'], 
                                                                       message="The image must be in jpg, jpeg or png format.")],
    widget = forms.FileInput(),
    label = "Portfolio Photo",
    required = False
  )
  title = forms.CharField(
    widget = forms.TextInput(attrs={'placeholder': 'Android Application Development For ABC.org'}),
    label = "Title",
    required = True
  )
  short_desc = forms.CharField(
    widget = forms.Textarea(attrs={'rows': 3, 'style': 'resize:none', 'placeholder': 'A very short description about your portfolio'}),
    label = "Short Description",
    help_text = "Limited to 250 characters",
    required = True
  )
  url = forms.CharField(
    widget = forms.TextInput(attrs={'placeholder': 'Link to your work if any'}),
    label = "Portfolio URL",
    required = False
  )
  tag = forms.MultipleChoiceField(
    choices=Tags.objects.values_list('id', 'name'),
    label="Tags (Multi-choice)",
    required=True,
  )
  
  class Meta:
    model = Portfolios
    fields = ['image_path', 'title', 'short_desc', 'url', 'tag']
  
  def clean(self):
    cleaned_data = super(UpdatePortfolioForm, self).clean()
    short_desc = cleaned_data.get("short_desc")
    if short_desc is not None and len(short_desc) > 250:
      self.add_error("short_desc", "Your short description is turning into an essay.")
    return cleaned_data