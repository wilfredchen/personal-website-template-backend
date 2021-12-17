from django.urls import path
from .import views

urlpatterns = [
  path('uiSetting', views.getUISetting),
  path('about', views.getAbout),
  path('experiences', views.getExp),
  path('educations', views.getEdu),
  path('certificates', views.getCert),
  path('skills', views.getSkill),
  path('contact', views.getContact),
  path('portfolios', views.getPortfolios),
  path('blog', views.getBlog),
  path('blog/<str:pk>', views.getBlogById),
]