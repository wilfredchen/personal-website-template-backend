from django.urls import path
from . import views

urlpatterns = [
  path('', views.homePage, name="home"),
  path('login/', views.loginPage, name="login"),
  path('logout/', views.logOutUser, name="logout"),
  path('experiences/', views.experiencesPage, name="experiences"),
  path('experiences/update/<str:pk>', views.updateExperiencesPage, name="update-experiences"),
  path('educations/', views.educationsPage, name="educations"),
  path('educations/update/<str:pk>', views.updateEducationsPage, name="update-educations"),
  ]