from rest_framework.serializers import ModelSerializer
from dashboard.models import User

class AboutSerializer(ModelSerializer):
  class Meta:
    model = User
    fields = ['name', 'email2', 'bio1', 'bio2', 'profile_photo', 'phone', 'linkedin_url', 'facebook_url', 'twitter_url', 'cv_path']