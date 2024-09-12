from django.shortcuts import render

# Create your views here.

def homePage(request):
    return render(request, 'solar/home.html' )

def aboutPage(request):
    return render(request, 'solar/about.html')

def servicesPage(request):
    return render(request, 'solar/services.html')

