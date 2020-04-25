from django.http import HttpResponse
from django.shortcuts import render

def HomePage(request):
    #return HttpResponse('home')
     return render(request,'HomePage.html')

def about(request):
    #return HttpResponse('about')
    return render(request, 'About.html')
