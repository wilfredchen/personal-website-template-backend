from rest_framework.decorators import api_view
from rest_framework.response import Response
from dashboard.models import User
from .serializers import AboutSerializer
from api import serializers

@api_view(['GET'])
def getRoutes(request):
  routes = [
    'GET /api/about'
  ]
  return Response(routes)

@api_view(['GET'])
def getAbout(request):
  user = User.objects.all().first()
  serializers = AboutSerializer(user)
  return Response(serializers.data)