from rest_framework.serializers import ModelSerializer
from dashboard.models import Certificates, Skills, UISetting, User, Experiences, Education

class UISettingSerializer(ModelSerializer):
  class Meta:
    model = UISetting
    fields = ['name', 'show']


class AboutSerializer(ModelSerializer):
  class Meta:
    model = User
    fields = ['name', 'email2', 'role', 'bio1', 'bio2', 'age', 'nationality', 'profile_photo', 'phone', 'linkedin_url', 'facebook_url', 'twitter_url', 'languages', 'current_resident', 'cv_path']
    

class ExpSerializer(ModelSerializer):
  class Meta:
    model = Experiences
    fields = ['year', 'title', 'company', 'short_desc', 'location']
    

class EduSerializer(ModelSerializer):
  class Meta:
    model = Education
    fields = ['year', 'major', 'school', 'grade', 'location']
    
    
class CertSerializer(ModelSerializer):
  class Meta:
    model = Certificates
    fields = ['year', 'title', 'award_body', 'url']
    
    
class SkillSerializer(ModelSerializer):
  class Meta:
    model = Skills
    fields = ['name', 'percentage']
    

class ContactSerializer(ModelSerializer):
  class Meta:
    model = User
    fields = ['email2','phone', 'linkedin_url', 'facebook_url', 'twitter_url']