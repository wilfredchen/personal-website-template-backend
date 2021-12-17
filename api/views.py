from rest_framework.decorators import api_view
from rest_framework.response import Response
from dashboard.models import Blog, Certificates, Education, Experiences, User, UISetting, Skills, Portfolios
from .serializers import AboutSerializer, BlogSerializer, ContactSerializer, PortfolioSerializer, UISettingSerializer, ExpSerializer, EduSerializer, CertSerializer, SkillSerializer
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

@api_view(['GET'])
def getPortfolios(request):
  portfolio = Portfolios.objects.all()
  serializers = PortfolioSerializer(portfolio, many = True)
  return Response(serializers.data)

@api_view(['GET'])
def getBlog(request):
  blog = Blog.objects.all()
  serializers = BlogSerializer(blog, many = True)
  return Response(serializers.data)

@api_view(['GET'])
def getBlogById(request, pk):
  blog = Blog.objects.get(id=pk)
  serializers = BlogSerializer(blog, many = False)
  return Response(serializers.data)
  