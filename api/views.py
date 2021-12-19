from rest_framework.decorators import api_view
from rest_framework.response import Response
from dashboard.models import Blog, Certificates, Education, Experiences, User, UISetting, Skills, Portfolios
from .serializers import AboutSerializer, BlogSerializer, ContactSerializer, PortfolioSerializer, UISettingSerializer, ExpSerializer, EduSerializer, CertSerializer, SkillSerializer, PaginationSerializer
from api import serializers
import math

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
def getBlog(request, page):
  totalCount = Blog.objects.all().count()
  perPage = 2
  currentPage = 1
  if page:
    currentPage = page
    
  totalPages = math.ceil(totalCount / perPage)
  start = (currentPage - 1) * perPage
  
  if currentPage == 1:
    blog = Blog.objects.all()[0:perPage]
    blogSerializer = BlogSerializer(blog, many=True).data
  else:
    blog = Blog.objects.all()[start: start + perPage]
    blogSerializer = BlogSerializer(blog, many=True).data
    
  pageData= [{"totalpages": totalPages, "currentpage": currentPage}]
  pageSerializer = PaginationSerializer(pageData, many=True).data
  return Response({
        "blog": blogSerializer,
        "page": pageSerializer
    })


@api_view(['GET'])
def getBlogById(request, pk):
  blog = Blog.objects.get(id=pk)
  serializers = BlogSerializer(blog, many = False)
  return Response(serializers.data)
  