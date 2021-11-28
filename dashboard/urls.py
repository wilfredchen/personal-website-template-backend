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
  path('certificates/', views.certificatePage, name="certificates"),
  path('certificates/update/<str:pk>', views.updateCertificatePage, name="update-certificate"),
  path('skills/', views.skillPage, name="skills"),
  path('skills/update/<str:pk>', views.updateSkillPage, name="update-skill"),
  path('tags/', views.tagPage, name="tags"),
  path('tags/update/<str:pk>', views.updateTagPage, name="update-tag"),
  path('portfolios/', views.portfolioPage, name="portfolios"),
  path('portfolios/update/<str:pk>', views.updatePortfolioPage, name="update-portfolio"),
  ]