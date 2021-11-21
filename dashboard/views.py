from django.shortcuts import render

# Create your views here.

def homePage(request):
  context = {}
  return render(request, 'dashboard/index.html', context)


def loginPage(request):
  context = {}
  return render(request, 'dashboard/login.html', context)


