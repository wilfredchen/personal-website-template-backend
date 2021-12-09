from rest_framework.decorators import api_view
from rest_framework.response import Response
from dashboard.models import Certificates, Education, Experiences, User, UISetting, Skills
from .serializers import AboutSerializer, ContactSerializer, UISettingSerializer, ExpSerializer, EduSerializer, CertSerializer, SkillSerializer
from api import serializers

@api_view(['GET'])
def getAbout(request):
  user = User.objects.all().first()
  serializers = AboutSerializer(user)
  return Response(serializers.data)


@api_view(['GET'])
def getUISetting(request):
  uiSetting = UISetting.objects.all()
  serializers = UISettingSerializer(uiSetting, many = True)
  return Response(serializers.data)


@api_view(['GET'])
def getExp(request):
  exp = Experiences.objects.all()
  serializers = ExpSerializer(exp, many = True)
  return Response(serializers.data)


@api_view(['GET'])
def getEdu(request):
  edu = Education.objects.all()
  serializers = EduSerializer(edu, many = True)
  return Response(serializers.data)


@api_view(['GET'])
def getCert(request):
  cert = Certificates.objects.all()
  serializers = CertSerializer(cert, many = True)
  return Response(serializers.data)


@api_view(['GET'])
def getSkill(request):
  skill = Skills.objects.all()
  serializers = SkillSerializer(skill, many = True)
  return Response(serializers.data)


@api_view(['GET'])
def getContact(request):
  contact = User.objects.all().first()
  serializers = ContactSerializer(contact)
  return Response(serializers.data)
